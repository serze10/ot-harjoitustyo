# Arkkitehtuuri

Seuraava kaavio kuvaa sovelluksen pääluokat ja niiden suhteet:

```mermaid
classDiagram
class DNAGui {
  - records: list
  - current_result: dict
  - seq_var: StringVar
  - seq_menu: OptionMenu
  - gc_var: BooleanVar
  - win_entry: Entry
  - step_entry: Entry
  - txt: Text
  + __init__()
  + open_fasta()
  + run_analysis()
  + _get_selected_record()
  + _compute_and_append_gc()
  + save_results()
}

class DNA_Tool {
  + read_fasta(path)
  + parse_fasta_string(s)
  + analyze_sequence(seq)
  + count_nucleotides(seq)
  + gc_content(seq)
  + calculate_gc_profile(seq, window, step)
  + save_results(path, results, fmt=None)
}

class RunDNA {
  + main(argv=None)
  + _process_record(header, seq, args)
}

DNAGui ..> DNA_Tool : uses
RunDNA ..> DNA_Tool : uses
DNA_Tool o-- parser : contains
DNA_Tool o-- analysis : contains

```

Kaavion perusteella `DNAGui` käyttää `DNA_Tool`-moduulia lukemaan FASTA-tiedostoja ja analysoimaan sekvenssejä. `RunDNA` on komentorivikäyttöliittymän päälogiikka, joka kutsuu samoja analysisyökaluja.
