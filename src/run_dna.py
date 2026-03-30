import sys
from dna_tool import read_fasta, analyze_sequence

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_dna.py path/to/file.fasta")
        sys.exit(1)

    path = sys.argv[1]
    recs = read_fasta(path)
    if not recs:
        print("No records found in", path)
        return

    for header, seq in recs:
        print(f'>{header}')
        a = analyze_sequence(seq)
        print('Length:', a['length'])
        print('Counts:', a['counts'])
        print('GC %:', a['gc_percent'])
        print()

if __name__ == '__main__':
    main()