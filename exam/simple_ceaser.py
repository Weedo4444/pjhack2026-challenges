"""Cezar: P = (C - shift) mod 26. None = przegląd 26 przesunięć."""
from solvers.classical import caesar, caesar_all

# DANE
CIPHERTEXT = 'AULEV{Zywj_ehpyej_dti_ectpd}'
SHIFT = None
PREFIX = 'PJATK{'

if __name__ == '__main__':
    if SHIFT is None:
        for k, plain in caesar_all(CIPHERTEXT, PREFIX):
            print(f'klucz={k:2}  {plain}')
    else:
        print(caesar(CIPHERTEXT, SHIFT))
