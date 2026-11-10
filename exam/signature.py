"""Podpis textbook RSA: s = m^d mod n (ćwiczenie, nie bezpieczny RSA-PSS)."""
from solvers.rsa import textbook_rsa_sign

# DANE
MESSAGE = 'zolw'
N = 4295229443
D = 2779181297

if __name__ == '__main__':
    signature = textbook_rsa_sign(MESSAGE.encode(), N, D)
    print(f'PJATK{{{signature:x}}}')
