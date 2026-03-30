from collections import Counter


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
