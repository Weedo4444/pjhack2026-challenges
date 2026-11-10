"""RSA Fermat: szukamy n = (a-b)(a+b) i odszyfrowujemy bloki."""
from solvers.rsa import decrypt_rsa_blocks
from solvers.encoding import as_text

# DANE
N = 100000246913740441219878966827008414657
E = 65537
BLOCKS = []   # wpisz liczby z tasks/RSA-fermat.py, np. int('abcd', 16)
P = None
Q = None
FERMAT_STEPS = 100000
BLOCK_SIZE = None  # jeśli bloki mają stałą liczbę bajtów

if __name__ == '__main__':
    if not BLOCKS:
        print('Uzupełnij BLOCKS danymi z tasks/RSA-fermat.py')
    else:
        plain, info = decrypt_rsa_blocks(N, E, BLOCKS, P, Q, FERMAT_STEPS, BLOCK_SIZE)
        print('Parametry:', info)
        print('Tekst:', as_text(plain))
