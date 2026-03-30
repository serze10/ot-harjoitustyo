import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath("src"))

import unittest
from dna_tool import parse_fasta_string



class TestDnaTool(unittest.TestCase):
    def test_parse_fasta_string_single(self):
        s = ">seq1\nACGTacgtNn\n"
        records = parse_fasta_string(s)
        self.assertEqual(len(records), 1)
        h, seq = records[0]
        self.assertEqual(h, "seq1")
        self.assertEqual(seq, "ACGTACGTNN")

if __name__ == "__main__":
    unittest.main()
