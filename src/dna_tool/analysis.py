from collections import Counter
import json
import csv
import os


VALID_BASES = set(["A", "C", "G", "T", "N"])


def count_nucleotides(seq):
    #Count nucleotides A/C/G/T/N in seq and returns a dict.
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
    #Return GC percentage computed over A/C/G/T bases. If none, returns 0.0.
    seq = seq.upper()
    counts = count_nucleotides(seq)
    atcg = counts["A"] + counts["C"] + counts["G"] + counts["T"]
    if atcg == 0:
        return 0.0
    gc = counts["G"] + counts["C"]
    return (gc / atcg) * 100


def analyze_sequence(seq):
    #Return a dictionary with length, counts and gc% for the given sequence.
    counts = count_nucleotides(seq)
    length = len(seq.replace("\n", ""))
    return {
        "length": length,
        "counts": counts,
        "gc_percent": round(gc_content(seq), 4),
    }


def calculate_gc_profile(seq, window=100, step=50):
    # Calculate GC content profile along the sequence using sliding windows.
    if window <= 0 or step <= 0:
        raise ValueError("window and step must be positive integers")
    s = seq.upper()
    return _sliding_windows_gc(s, window, step)


def _sliding_windows_gc(s, window, step):
    #Returns (positions, gc_values)
    
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
    # Save results to a JSON file. Creates parent directories if needed.
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)


def save_results_csv(path, results):
    # Save results to a CSV file. Creates parent directories if needed.
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
    # Save results to a file in json or csv.
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
    #Write summary and GC profile for a single results dict.
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
    #Write summary table for multiple result records.
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
