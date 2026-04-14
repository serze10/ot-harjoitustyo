import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath("src"))

from dna_tool import analyze_sequence, calculate_gc_profile, save_results_json, save_results_csv


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

    def test_gc_profile_shorter_than_window(self):
        seq = "ACG"
        positions, gc = calculate_gc_profile(seq, window=10, step=5)
        # sequence shorter than window should produce one window starting at 0
        self.assertEqual(positions, [0])
        self.assertEqual(len(gc), 1)

    def test_analyze_sequence_with_invalid_chars(self):
        # invalid characters should be treated as 'N'
        seq = "ACGTXYZ"
        res = analyze_sequence(seq)
        counts = res["counts"]
        # X, Y, Z -> counted as N
        self.assertGreaterEqual(counts.get("N", 0), 3)


if __name__ == "__main__":
    unittest.main()
