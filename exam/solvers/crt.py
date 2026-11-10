"""Uogólnione CRT; działa również dla nieskoprzymych, zgodnych modułów."""
from math import gcd


def solve_crt(moduli: list[int], residues: list[int]) -> tuple[int, int]:
    if not moduli or len(moduli) != len(residues):
        raise ValueError('Nierówna liczba modułów i reszt')
    x, product = 0, 1
    for m, r in zip(moduli, residues):
        if m <= 0:
            raise ValueError('Moduł musi być dodatni')
        common = gcd(product, m)
        if (r-x) % common:
            raise ValueError('Sprzeczne kongruencje')
        part = m // common
        t = ((r-x)//common * pow(product//common, -1, part)) % part if part > 1 else 0
        x = (x + product*t) % (product*part)
        product *= part
    return x, product
