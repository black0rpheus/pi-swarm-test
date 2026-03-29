"""Command-line interface for pi-calc."""

from __future__ import annotations

import argparse

from pi_calc.pi import compute_pi


def main(argv: list[str] | None = None) -> None:
    """Entry point for the ``pi-calc`` CLI."""
    parser = argparse.ArgumentParser(
        prog="pi-calc",
        description="Approximate the value of pi using the Leibniz formula.",
    )
    parser.add_argument(
        "-n",
        "--iterations",
        type=int,
        default=1_000_000,
        help="Number of iterations (default: 1,000,000). More iterations = better accuracy.",
    )
    args = parser.parse_args(argv)

    result = compute_pi(args.iterations)
    print(f"Pi ≈ {result}")
    print(f"(using {args.iterations:,} iterations)")


if __name__ == "__main__":
    main()
