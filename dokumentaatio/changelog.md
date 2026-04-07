## Viikko 3

- Lisätty DNA-analyysityökalu: FASTA-parser ja perusanalyysi (pituus, A/C/G/T, GC%).
- Lisätty `run_dna.py`-ajoskripti ja `src/dna_tool`-paketti.
- Lisätty yksikkötesti `tests/test_dna_tool.py` parsaukselle.
- Lisätty Invoke-tehtävät `tasks.py` (start, test, coverage-report).
- Lisätty `.coveragerc` testikattavuuden konfigurointia varten.
- Lisätty changelog-tiedosto ja READMEHarjoitustyö 6: Changelog

## Viikko 4

- Lisätty GC‑profiilin laskenta liukuvalla ikkunalla: `calculate_gc_profile(sequence, window, step)`.
	- Funktio palauttaa `(positions, gc_values)`  ikkunoiden aloitusindeksit ja vastaavat
		GC‑prosentit.
- Lisätty analyysitulosten tallennus JSON/CSV: `save_results(path, results, fmt=None)`,
	`save_results_json` ja `save_results_csv`.
- Laajennettu CLI‑skriptiä `src/run_dna.py` seuraavilla lipuilla:
	- `--gc-profile` laskee GC‑profiilin (parametrit `--window` ja `--step`).
	- `--save-results PATH` tallentaa tulokset (päätteestä päätellään formaatti),
		mahdollisuus pakottaa formaatti `--save-format {json,csv}`.
- Lisätty yksikkötestit `tests/test_analysis.py` GC‑profiilille ja tallennukselle.
- Paranneltu CSV‑muotoilua: tukee sekä yksittäisen että usean sekvenssin
	tallennusta (erillinen yhteenveto- ja profiiliosa).
- Korjattu lint‑varoituksia ja parannettu koodin rakennetta:
	- Hajotettu suurempia funktioita apufunktioiksi (`_sliding_windows_gc`,
		`_write_single_summary`, `_write_multiple_summary`, `_process_record`).



Dokumentaatioon lisätty myös lyhyt käyttöohje CLI:lle ja testiohjeet.
