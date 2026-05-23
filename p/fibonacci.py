"""Simple Fibonacci series generator and CLI.

Usage:
    python p/fibonacci.py 10

If no argument is given, prints first 10 Fibonacci numbers.
"""

from typing import List
import sys


def fibonacci(n: int) -> List[int]:
    """Return the first n Fibonacci numbers (n >= 0)."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Please provide an integer for the number of terms.")
        sys.exit(1)

    seq = fibonacci(n)
    print("Fibonacci series (first {} terms):".format(n))
    print(" ".join(str(x) for x in seq))
