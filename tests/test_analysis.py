import os
import sys
import tempfile
import unittest
from types import SimpleNamespace

sys.path.insert(0, os.path.abspath("src"))

from dna_tool import (
    parse_fasta_string,
    count_nucleotides,
    gc_content,
    analyze_sequence,
    calculate_gc_profile,
    save_results,
    save_results_json,
    save_results_csv,
    find_motif,
)

from run_dna import _process_record


class TestAnalysis(unittest.TestCase):
    def test_calculate_gc_profile_simple(self):
        seq = "ACGTACGT"
        positions, gc = calculate_gc_profile(seq, window=4, step=2)
        self.assertEqual(positions, [0, 2, 4])
        self.assertEqual(gc, [50.0, 50.0, 50.0])

    def test_save_results_json_and_csv(self):
        seq = "ACGTACGT"
        res = analyze_sequence(seq)
        pos, gc = calculate_gc_profile(seq, window=4, step=2)
        res["gc_profile"] = list(zip(pos, gc))

        td = tempfile.mkdtemp()
        jpath = os.path.join(td, "out.json")
        cpath = os.path.join(td, "out.csv")

        save_results_json(jpath, res)
        self.assertTrue(os.path.exists(jpath))

        save_results_csv(cpath, res)
        self.assertTrue(os.path.exists(cpath))

    def test_analyze_sequence_with_invalid_chars(self):
        seq = "ACGTXYZ"
        res = analyze_sequence(seq)
        counts = res["counts"]
        self.assertGreaterEqual(counts.get("N", 0), 3)

    def test_calculate_gc_profile_invalid_args(self):
        with self.assertRaises(ValueError):
            calculate_gc_profile("ACGT", window=0, step=1)
        with self.assertRaises(ValueError):
            calculate_gc_profile("ACGT", window=1, step=0)

    def test_find_motif_overlapping(self):
        seq = "AAAA"
        pos = find_motif(seq, "AA")
        self.assertEqual(pos, [0, 1, 2])

    def test_run_process_record_returns_profile(self):
        args = SimpleNamespace(gc_profile=True, window=4, step=2, save_results=None, save_format=None)
        result = _process_record("h", "ACGTACGT", args)
        self.assertIn("header", result)
        self.assertIn("length", result)
        self.assertIn("gc_percent", result)
        self.assertIn("gc_profile", result)


if __name__ == "__main__":
    unittest.main()
