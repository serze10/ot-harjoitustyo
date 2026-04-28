from collections import Counter
import json
import csv
import os


VALID_BASES = set(["A", "C", "G", "T", "N"])


def count_nucleotides(seq):
    """Count nucleotides A/C/G/T/N in ``seq`` and return a dict.

    Any unknown character is counted as 'N'. The returned dict contains
    keys for ``A``, ``C``, ``G``, ``T`` and ``N`` with integer counts.
    """
    seq = seq.upper()
    c = Counter()
    for i in seq:
        if i in VALID_BASES:
            c[i] += 1
        else:
            # Treat any unknown character as 'N' to keep counts bounded
            c['N'] += 1
    return {base: c.get(base, 0) for base in ["A", "C", "G", "T", "N"]}


def gc_content(seq):
    """Return GC percentage computed over A/C/G/T bases.

    Non-ATCG characters are treated as 'N' and excluded from the
    denominator. Returns 0.0 if there are no A/C/G/T bases.
    """
    seq = seq.upper()
    counts = count_nucleotides(seq)
    atcg = counts["A"] + counts["C"] + counts["G"] + counts["T"]
    if atcg == 0:
        return 0.0
    gc = counts["G"] + counts["C"]
    return (gc / atcg) * 100


def analyze_sequence(seq):
    """Analyze ``seq`` and return a summary dictionary.

    The returned dict contains the sequence ``length`` (excluding newlines),
    nucleotide ``counts``, and ``gc_percent`` rounded to 4 decimals.
    """
    counts = count_nucleotides(seq)
    length = len(seq.replace("\n", ""))
    return {
        "length": length,
        "counts": counts,
        "gc_percent": round(gc_content(seq), 4),
    }


def calculate_gc_profile(seq, window=100, step=50):
    """Calculate GC content profile along ``seq`` using sliding windows.

    ``window`` and ``step`` must be positive integers. Returns a tuple
    ``(positions, gc_values)`` where positions are 0-based window start
    indices and gc_values are GC percentages for each window.
    """
    if window <= 0 or step <= 0:
        raise ValueError("window and step must be positive integers")
    s = seq.upper()
    return _sliding_windows_gc(s, window, step)


def _sliding_windows_gc(s, window, step):
    """Internal helper: return ``(positions, gc_values)`` for sliding windows.

    ``s`` is expected to be an uppercase sequence string.
    """
    n = len(s)
    positions = []
    gc_values = []
    if n < window:
        # Single window covering the whole sequence
        positions.append(0)
        gc_values.append(round(gc_content(s), 4))
        return positions, gc_values

    i = 0
    while i + window <= n:
        window_seq = s[i : i + window]
        positions.append(i)
        gc_values.append(round(gc_content(window_seq), 4))
        i += step

    if positions and positions[-1] + window < n:
        i = n - window
        if i != positions[-1]:
            window_seq = s[i : i + window]
            positions.append(i)
            gc_values.append(round(gc_content(window_seq), 4))

    return positions, gc_values


def save_results_json(path, results):
    """Save ``results`` to a JSON file at ``path``.

    Parent directories are created if they do not exist. The JSON is
    written with indentation and UTF-8 encoding.
    """
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)


def save_results_csv(path, results):
    """Save ``results`` to a CSV file at ``path``.

    If ``results`` is a list, a summary table is written followed by a
    per-window GC profile section. Parent directories are created when
    necessary.
    """
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        if isinstance(results, list):
            _write_multiple_summary(writer, results)
            writer.writerow([])
            writer.writerow(["header", "position", "gc_percent"])
            for rec in results:
                for pos, gc in rec.get("gc_profile", []) if rec.get("gc_profile") else []:
                    writer.writerow([rec.get("header"), pos, gc])
        else:
            _write_single_summary(writer, results)



def save_results(path, results, fmt=None):
    """Save analysis ``results`` to ``path`` using JSON or CSV format.

    The format can be provided explicitly via ``fmt`` ("json" or "csv");
    if omitted it is inferred from the file extension.
    """
    if fmt is None:
        _, ext = os.path.splitext(path)
        fmt = ext.lstrip(".").lower()
    if fmt == "json":
        save_results_json(path, results)
    elif fmt == "csv":
        save_results_csv(path, results)
    else:
        raise ValueError(f"Unsupported format: {fmt!r}")


def _write_single_summary(writer, results):
    """Write summary and GC profile for a single results dict to CSV.

    The writer is a csv.writer instance.
    """
    writer.writerow(["metric", "value"])
    writer.writerow(["length", results.get("length")])
    counts = results.get("counts", {})
    for base in ["A", "C", "G", "T", "N"]:
        writer.writerow([f"count_{base}", counts.get(base)])
    writer.writerow(["gc_percent", results.get("gc_percent")])
    writer.writerow([])
    # gc profile
    writer.writerow(["position", "gc_percent"])
    for pos, gc in results.get("gc_profile", []) if results.get("gc_profile") else []:
        writer.writerow([pos, gc])


def _write_multiple_summary(writer, results):
    """Write a summary table for multiple result records to CSV.

    The writer is a csv.writer instance. Each row contains header,
    length, base counts and gc_percent.
    """
    header_row = [
        "header",
        "length",
        "count_A",
        "count_C",
        "count_G",
        "count_T",
        "count_N",
        "gc_percent",
    ]
    writer.writerow(header_row)
    for rec in results:
        counts = rec.get("counts", {})
        writer.writerow([
            rec.get("header"),
            rec.get("length"),
            counts.get("A"),
            counts.get("C"),
            counts.get("G"),
            counts.get("T"),
            counts.get("N"),
            rec.get("gc_percent"),
        ])


def find_motif(seq: str, motif: str) -> list:
    """Find all (possibly overlapping) occurrences of `motif` in `seq`.

    Returns a list of 0-based start positions. Both `seq` and `motif` are
    compared case-insensitively. If motif is empty, returns an empty list.
    """
    if not motif:
        return []
    s = seq.upper()
    m = motif.upper()
    positions = []
    start = 0
    while True:
        idx = s.find(m, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1  # allow overlapping matches
    return positions
