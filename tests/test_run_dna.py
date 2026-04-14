import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath("src"))

from run_dna import main as run_main


def test_run_dna_outputs_gc_profile(capsys):
    in_fasta = "src/testfasta/testi.fasta"

    rc = run_main([in_fasta, "--gc-profile"])
    assert rc == 0

    captured = capsys.readouterr()
    out = captured.out
    assert ">" in out
    assert "GC profile windows" in out