import json
import tkinter as tk

from gui import DNAGui


def _mock_noop(*a, **k):
    return None


def test_open_fasta_and_run_analysis(monkeypatch, tmp_path):
    fasta = tmp_path / "test.fasta"
    fasta.write_text(
        ">seq1\nATGCGTATGCGT\n"
    )

    # mock dialogs to use our file and suppress message boxes
    monkeypatch.setattr("tkinter.filedialog.askopenfilename", lambda **kw: str(fasta))
    monkeypatch.setattr("tkinter.messagebox.showerror", _mock_noop)
    monkeypatch.setattr("tkinter.messagebox.showinfo", _mock_noop)

    gui = DNAGui()
    gui.withdraw()
    gui.open_fasta()
    gui.run_analysis()

    assert hasattr(gui, "current_result")
    res = gui.current_result
    assert res["length"] == 12
    # output text must contain Length
    out = gui.txt.get("1.0", tk.END)
    assert "Length: 12" in out


def test_find_motif(monkeypatch, tmp_path):
    fasta = tmp_path / "test2.fasta"
    fasta.write_text(
        ">h\nATGATGATGATG\n"
    )
    monkeypatch.setattr("tkinter.filedialog.askopenfilename", lambda **kw: str(fasta))
    monkeypatch.setattr("tkinter.messagebox.showinfo", _mock_noop)
    monkeypatch.setattr("tkinter.messagebox.showerror", _mock_noop)

    gui = DNAGui()
    gui.withdraw()
    gui.open_fasta()

    gui.motif_entry.delete(0, tk.END)
    gui.motif_entry.insert(0, "ATG")
    gui.find_motif()

    out = gui.txt.get("1.0", tk.END)
    assert "Motif search" in out
    assert "Positions (0-based):" in out


def test_save_results_json(monkeypatch, tmp_path):
    fasta = tmp_path / "save.fasta"
    fasta.write_text(
        ">s\nACGTACGTACGT\n"
    )
    monkeypatch.setattr("tkinter.filedialog.askopenfilename", lambda **kw: str(fasta))
    monkeypatch.setattr("tkinter.messagebox.showinfo", _mock_noop)
    monkeypatch.setattr("tkinter.messagebox.showerror", _mock_noop)

    gui = DNAGui()
    gui.withdraw()
    gui.open_fasta()
    gui.run_analysis()

    outpath = tmp_path / "out.json"
    monkeypatch.setattr("tkinter.filedialog.asksaveasfilename", lambda **kw: str(outpath))

    gui.save_results()

    assert outpath.exists()
    data = json.loads(outpath.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    assert data.get("length") == 12
