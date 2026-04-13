import json
import tkinter as tk
from tkinter import filedialog, messagebox

try:
    # optional plotting
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except Exception:
    HAS_MATPLOTLIB = False

from dna_tool import (
    read_fasta,
    analyze_sequence,
    calculate_gc_profile,
    save_results,
)


class DNAGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DNA Analysis Tool")
        self.geometry("800x600")

        self._build_widgets()
        self.records = []

    def _build_widgets(self):
        frm_top = tk.Frame(self)
        frm_top.pack(fill=tk.X, padx=8, pady=8)

        btn_open = tk.Button(frm_top, text="Open FASTA", command=self.open_fasta)
        btn_open.pack(side=tk.LEFT)

        self.seq_var = tk.StringVar()
        self.seq_menu = tk.OptionMenu(frm_top, self.seq_var, "")
        self.seq_menu.pack(side=tk.LEFT, padx=8)

        self.gc_var = tk.BooleanVar(value=True)
        chk_gc = tk.Checkbutton(frm_top, text="Compute GC profile", variable=self.gc_var)
        chk_gc.pack(side=tk.LEFT, padx=8)

        tk.Label(frm_top, text="Window:").pack(side=tk.LEFT)
        self.win_entry = tk.Entry(frm_top, width=6)
        self.win_entry.insert(0, "100")
        self.win_entry.pack(side=tk.LEFT)

        tk.Label(frm_top, text="Step:").pack(side=tk.LEFT)
        self.step_entry = tk.Entry(frm_top, width=6)
        self.step_entry.insert(0, "50")
        self.step_entry.pack(side=tk.LEFT)

        btn_run = tk.Button(frm_top, text="Run", command=self.run_analysis)
        btn_run.pack(side=tk.LEFT, padx=8)

        btn_save = tk.Button(frm_top, text="Save Results...", command=self.save_results)
        btn_save.pack(side=tk.LEFT, padx=8)

        if HAS_MATPLOTLIB:
            btn_plot = tk.Button(frm_top, text="Plot GC", command=self.plot_gc)
            btn_plot.pack(side=tk.LEFT, padx=8)

        # Text output
        self.txt = tk.Text(self, wrap=tk.NONE)
        self.txt.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    def open_fasta(self):
        path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta *.fa *"), ("All files", "*")])
        if not path:
            return
        try:
            recs = read_fasta(path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read FASTA: {e}")
            return
        self.records = recs
        menu = self.seq_menu["menu"]
        menu.delete(0, "end")
        for h, _ in recs:
            menu.add_command(label=h, command=lambda v=h: self.seq_var.set(v))
        if recs:
            self.seq_var.set(recs[0][0])
        self.txt.insert(tk.END, f"Loaded {len(recs)} records from {path}\n")

    def _get_selected_record(self):
        name = self.seq_var.get()
        for h, seq in self.records:
            if h == name:
                return h, seq
        if self.records:
            return self.records[0]
        return None, None

    def run_analysis(self):
        header, seq = self._get_selected_record()
        if not seq:
            messagebox.showinfo("No sequence", "Open a FASTA and select a sequence first")
            return
        try:
            window = int(self.win_entry.get())
            step = int(self.step_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Window and step must be integers")
            return

        analysis = analyze_sequence(seq)
        output = [f">{header}", f"Length: {analysis['length']}", f"Counts: {analysis['counts']}", f"GC %: {analysis['gc_percent']}"]

        if self.gc_var.get():
            positions, gc_vals = calculate_gc_profile(seq, window=window, step=step)
            analysis["gc_profile"] = list(zip(positions, gc_vals))
            output.append(f"GC profile windows: {len(positions)}")
            output.append(f"First windows (pos,gc): {analysis['gc_profile'][:10]}")

        self.current_result = {"header": header, **analysis}
        self.txt.insert(tk.END, "\n".join(output) + "\n\n")

    def save_results(self):
        if not hasattr(self, "current_result"):
            messagebox.showinfo("No results", "Run analysis before saving")
            return
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json"), ("CSV", "*.csv")])
        if not path:
            return
        # if user chose csv extension but provided .json override not supported here; save_results will infer
        try:
            save_results(path, self.current_result)
        except Exception as e:
            messagebox.showerror("Save failed", str(e))
            return
        messagebox.showinfo("Saved", f"Results saved to {path}")

    def plot_gc(self):
        if not HAS_MATPLOTLIB:
            messagebox.showinfo("Not available", "matplotlib not installed")
            return
        if not hasattr(self, "current_result"):
            messagebox.showinfo("No results", "Run analysis before plotting")
            return
        profile = self.current_result.get("gc_profile")
        if not profile:
            messagebox.showinfo("No profile", "GC profile not available")
            return
        positions, gc_vals = zip(*profile)
        plt.figure(figsize=(8, 3))
        plt.plot(positions, gc_vals, marker="o")
        plt.xlabel("Position")
        plt.ylabel("GC %")
        plt.title(f"GC profile: {self.current_result.get('header')}")
        plt.grid(True)
        plt.show()


def main():
    app = DNAGui()
    app.mainloop()


if __name__ == "__main__":
    main()
