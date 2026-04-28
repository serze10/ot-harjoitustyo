"""Command-line entry point for simple DNA analyses.

This module provides ``main()`` which parses CLI arguments and calls the
dna_tool analysis functions to print summaries and optionally save results.
"""

import argparse
import sys
from dna_tool import (
    read_fasta,
    analyze_sequence,
    calculate_gc_profile,
    save_results,
)


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Simple DNA analysis CLI",
    )
    p.add_argument("fasta", help="Path to FASTA file")
    p.add_argument(
        "--gc-profile",
        action="store_true",
        help="Compute GC profile using sliding window",
    )
    p.add_argument(
        "--window",
        type=int,
        default=100,
        help="Sliding window size (default: 100)",
    )
    p.add_argument(
        "--step",
        type=int,
        default=50,
        help="Sliding window step (default: 50)",
    )
    p.add_argument(
        "--save-results",
        metavar="PATH",
        help=(
            "Save results to PATH (JSON or CSV by extension)."
        ),
    )
    p.add_argument(
        "--save-format",
        choices=["json", "csv"],
        help="Force save format (overrides extension)",
    )

    args = p.parse_args(argv)

    recs = read_fasta(args.fasta)
    if not recs:
        print(f"No records found in {args.fasta}")
        return 1

    all_results = []
    for header, seq in recs:
        result = _process_record(header, seq, args)
        all_results.append(result)

    if args.save_results:
        to_save = all_results[0] if len(all_results) == 1 else all_results
        save_results(args.save_results, to_save, fmt=args.save_format)
        print(f"Saved results to {args.save_results}")

    return 0


def _process_record(header, seq, args):
    """Analyze a single record, optionally compute GC profile and print summary.

    Returns a dict suitable for saving (contains header and analysis keys).
    """
    print(f">{header}")
    analysis = analyze_sequence(seq)
    print(f"Length: {analysis['length']}")
    print(f"Counts: {analysis['counts']}")
    print(f"GC %: {analysis['gc_percent']}")

    if args.gc_profile:
        positions, gc_vals = calculate_gc_profile(
            seq, window=args.window, step=args.step
        )
        analysis["gc_profile"] = list(zip(positions, gc_vals))
        print(f"GC profile windows: {len(positions)}")
        print(f"First windows (pos,gc): {analysis['gc_profile'][:5]}")

    print()
    return {"header": header, **analysis}


if __name__ == '__main__':
    sys.exit(main())
