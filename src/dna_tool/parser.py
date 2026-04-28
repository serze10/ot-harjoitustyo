def parse_fasta_string(s):
    """Parse a FASTA-formatted string and return a list of (header, sequence) tuples.

    Empty lines are ignored. Sequence lines are concatenated and returned in
    upper-case. Headers are the text following the leading '>' on header lines.
    """
    records = []
    header = None
    seq_lines = []

    for line in s.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if header is not None:
                records.append((header, "".join(seq_lines).upper()))
            header = line[1:].strip()
            seq_lines = []
        else:
            seq_lines.append(line)

    if header is not None:
        records.append((header, "".join(seq_lines).upper()))

    return records


def read_fasta(path):
    """Read a FASTA file from ``path`` and return list of (header, sequence).

    The file is read using UTF-8 encoding and parsed with
    :func:`parse_fasta_string`.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return parse_fasta_string(content)
