def parse_fasta_string(s):
    """Parses a FASTA string and returns a list of (header, sequence) tuples.

    Sequences are returned as uppercase strings with whitespace/newlines removed.
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
    #Reads a FASTA file from path and returns list of (header, sequence).
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return parse_fasta_string(content)
