"""Dydaktyczne RSA (Fermat) oraz podpis typu textbook RSA."""
from math import isqrt, gcd
from .encoding import int_bytes


def fermat_factor(n: int, steps: int = 100000):
    if n < 4:
        raise ValueError('Zbyt małe n')
    if n % 2 == 0:
        return 2, n // 2
    a = isqrt(n)
    if a*a < n:
        a += 1
    for _ in range(steps):
        b2 = a*a - n
        b = isqrt(b2)
        if b*b == b2:
            p, q = a-b, a+b
            if p > 1 and p*q == n:
                return p, q
        a += 1
    return None


def decrypt_rsa_blocks(n: int, e: int, blocks: list[int], p: int | None = None,
                       q: int | None = None, steps: int = 100000,
                       block_size: int | None = None):
    if p is None or q is None:
        factors = fermat_factor(n, steps)
        if factors is None:
            raise ValueError('Fermat nie znalazł czynników w limicie')
        p, q = factors
    if p*q != n:
        raise ValueError('p * q != n')
    phi = (p-1)*(q-1)
    if gcd(e, phi) != 1:
        raise ValueError('e nie ma odwrotności modulo phi')
    d = pow(e, -1, phi)
    raw = b''.join(int_bytes(pow(c, d, n), block_size) for c in blocks)
    return raw, {'p': p, 'q': q, 'd': d}


def textbook_rsa_sign(message: bytes, n: int, d: int) -> int:
    return pow(int.from_bytes(message, 'big'), d, n)
