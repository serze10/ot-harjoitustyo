# Arkkitehtuuri

Seuraava kaavio kuvaa sovelluksen pääluokat ja niiden suhteet (+ = public ja - = private):

```mermaid
classDiagram
package "dna_tool" {
  class parser {
    + parse_fasta_string(s)
    + read_fasta(path)
  }
  class analysis {
    + analyze_sequence(seq)
    + count_nucleotides(seq)
    + gc_content(seq)
    + calculate_gc_profile(seq, window, step)
    + save_results(path, results, fmt=None)
  }
}

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

class RunDNA {
  + main(argv=None)
  + _process_record(header, seq, args)
}

DNAGui ..> parser : uses
DNAGui ..> analysis : uses
RunDNA ..> parser : uses
RunDNA ..> analysis : uses

```

Kaavion perusteella `dna_tool` on paketti, joka sisältää erilliset `parser`- ja `analysis`-moduulit. `DNAGui` ja `RunDNA` käyttävät suoraan näitä moduuleja: `parser` lukee FASTA-tiedostot ja `analysis` laskee tilastot ja tallentaa tulokset.
