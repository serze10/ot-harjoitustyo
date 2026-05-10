import tkinter as tk
from tkinter import filedialog, messagebox

from dna_tool import analysis
import dna_tool


class DNAGui(tk.Tk):
    def __init__(self):
        """Initialize the GUI window and internal state, then build widgets."""
        super().__init__()
        self.title("DNA Analysis Tool")
        self.geometry("800x600")
        self.records = []
        self.current_result = None
        self.seq_var = None
        self.seq_menu = None
        self.gc_var = None
        self.win_entry = None
        self.step_entry = None
        self.txt = None

        self._build_widgets()

    def _build_widgets(self):
        """Build the top control bar and the main text widget."""
        self._build_top_widgets()
        self._build_text_widget()

    def _build_top_widgets(self):
        """Create and pack the top frame containing controls and inputs."""
        frm_top = tk.Frame(self)
        frm_top.pack(fill=tk.X, padx=8, pady=8)
        self._add_open_button(frm_top)
        self._add_seq_menu(frm_top)
        self._add_gc_checkbox(frm_top)
        self._add_entry(frm_top, "Window:", "100", "win_entry")
        self._add_entry(frm_top, "Step:", "50", "step_entry")
        self._add_entry(frm_top, "Motif:", "", "motif_entry")
        self._add_run_and_save(frm_top)

    def _add_open_button(self, parent):
        """Add a button to open a FASTA file and populate sequences."""
        btn_open = tk.Button(parent, text="Open FASTA", command=self.open_fasta)
        btn_open.pack(side=tk.LEFT)

    def _add_seq_menu(self, parent):
        """Add an OptionMenu for selecting a sequence from the loaded FASTA."""
        self.seq_var = tk.StringVar()
        self.seq_menu = tk.OptionMenu(parent, self.seq_var, "")
        self.seq_menu.pack(side=tk.LEFT, padx=8)

    def _add_gc_checkbox(self, parent):
        """Add a checkbox to toggle GC profile computation on/off."""
        self.gc_var = tk.BooleanVar(value=True)
        chk_gc = tk.Checkbutton(parent, text="Compute GC profile", variable=self.gc_var)
        chk_gc.pack(side=tk.LEFT, padx=8)

    def _add_entry(self, parent, label_text, default, attr_name):
        """Add a labeled Entry and store it on ``self`` as ``attr_name``."""
        tk.Label(parent, text=label_text).pack(side=tk.LEFT)
        ent = tk.Entry(parent, width=6)
        ent.insert(0, default)
        ent.pack(side=tk.LEFT)
        setattr(self, attr_name, ent)

    def _add_run_and_save(self, parent):
        """Add Run/Save/Find Motif buttons to the parent frame."""
        btn_run = tk.Button(parent, text="Run", command=self.run_analysis)
        btn_run.pack(side=tk.LEFT, padx=8)
        btn_save = tk.Button(parent, text="Save Results...", command=self.save_results)
        btn_save.pack(side=tk.LEFT, padx=8)
        btn_motif = tk.Button(parent, text="Find Motif", command=self.find_motif)
        btn_motif.pack(side=tk.LEFT, padx=8)

    def _build_text_widget(self):
        """Create the main text area used for output and logs."""
        self.txt = tk.Text(self, wrap=tk.NONE)
        self.txt.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    def open_fasta(self):
        """Open a FASTA file and populate the sequence selection menu."""
        filetypes = [("FASTA files", "*.fasta *.fa *"), ("All files", "*")]
        path = filedialog.askopenfilename(filetypes=filetypes)
        if not path:
            return
        try:
            recs = dna_tool.read_fasta(path)
        except (OSError, UnicodeError) as exc:
            messagebox.showerror("Error", f"Failed to read FASTA: {exc}")
            return
        self._populate_seq_menu(recs, path)

    def _populate_seq_menu(self, recs, path):
        """Populate the sequence OptionMenu and store records."""
        self.records = recs
        menu = self.seq_menu["menu"]
        menu.delete(0, "end")
        for h, _ in recs:
            menu.add_command(label=h, command=lambda v=h: self.seq_var.set(v))
        if recs:
            self.seq_var.set(recs[0][0])
        self.txt.insert(tk.END, f"Loaded {len(recs)} records from {path}\n")

    def _get_selected_record(self):
        """Return the currently selected (header, sequence) tuple.

        Falls back to the first record if the selection is missing.
        """
        name = self.seq_var.get()
        for h, seq in self.records:
            if h == name:
                return h, seq
        if self.records:
            return self.records[0]
        return None, None

    def run_analysis(self):
        """Run analysis on the selected sequence and append results to text."""
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
        result = dna_tool.analyze_sequence(seq)
        output = self._format_analysis_output(header, result)

        if self.gc_var.get():
            gc_lines = self._compute_and_append_gc(result, seq, window, step)
            output.extend(gc_lines)

        self.current_result = {"header": header, **result}
        self.txt.insert(tk.END, "\n".join(output) + "\n\n")

    def _format_analysis_output(self, header, result):
        """Return a list of text lines summarizing an analysis result."""
        out = [f">{header}", f"Length: {result['length']}"]
        out.append(f"Counts: {result['counts']}")
        out.append(f"GC %: {result['gc_percent']}")
        return out

    def _compute_and_append_gc(self, result, seq, window, step):
        """Compute GC profile and return summary lines.

        The function updates ``result`` with key ``gc_profile`` and
        returns a list of text lines describing the profile summary.
        """
        positions, gc_vals = dna_tool.calculate_gc_profile(seq, window=window, step=step)
        result["gc_profile"] = list(zip(positions, gc_vals))
        lines = [f"GC profile windows: {len(positions)}"]
        first_windows = result["gc_profile"][:10]
        lines.append(f"First windows (pos,gc): {first_windows}")
        return lines

    def save_results(self):
        """Save the current analysis result to JSON or CSV chosen by user."""
        if not getattr(self, "current_result", None):
            messagebox.showinfo("No results", "Run analysis before saving")
            return
        save_types = [("JSON", "*.json"), ("CSV", "*.csv")]
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=save_types)
        if not path:
            return
        try:
            dna_tool.save_results(path, self.current_result)
        except (OSError, ValueError) as exc:
            messagebox.showerror("Save failed", str(exc))
            return
        messagebox.showinfo("Saved", f"Results saved to {path}")

    def find_motif(self):
        """Search the selected sequence for a user-provided motif and show positions."""
        header, seq = self._get_selected_record()
        if not seq:
            messagebox.showinfo("No sequence", "Open a FASTA and select a sequence first")
            return
        motif = ""
        if hasattr(self, 'motif_entry') and self.motif_entry:
            motif = self.motif_entry.get().strip()
        if not motif:
            messagebox.showinfo("No motif", "Enter a motif string first")
            return
        pos = analysis.find_motif(seq, motif)

        if not pos:
            messagebox.showinfo("No matches", f"Motif '{motif}' not found in sequence {header}")
            return

        # Display results in the text area (show all positions)
        self.txt.insert(tk.END, f"Motif search: '{motif}' in {header} -> {len(pos)} matches\n")
        # Print positions with line breaks every 25 entries for readability
        self.txt.insert(tk.END, "Positions (0-based):\n")
        for i in range(0, len(pos), 25):
            chunk = pos[i : i + 25]
            line = ", ".join(str(p) for p in chunk)
            self.txt.insert(tk.END, line + "\n")
        self.txt.insert(tk.END, "\n")

def main():
    app = DNAGui()
    app.mainloop()


if __name__ == "__main__":
    main()
