"""ElGamal: m = b * (a^x)^(-1) mod p, przeszukiwanie małego przedziału x."""
from solvers.elgamal import parse_pairs, decrypt_elgamal, search_elgamal
from solvers.encoding import as_text

# DANE
P = 10007
CIPHERTEXT_HEX = ''  # pełny hex z tasks/el_gamal.py
WORD_CHARS = 4
KEY = None
START = 2100
END = 2200
PREFIX = b'PJATK{'

if __name__ == '__main__':
    if not CIPHERTEXT_HEX:
        print('Uzupełnij CIPHERTEXT_HEX z tasks/el_gamal.py')
    else:
        pairs = parse_pairs(CIPHERTEXT_HEX, WORD_CHARS)
        if KEY is not None:
            numbers = decrypt_elgamal(P, pairs, KEY)
            print(as_text(bytes(numbers)) if all(n < 256 for n in numbers) else numbers)
        else:
            for key, plain in search_elgamal(P, pairs, START, END, PREFIX):
                print(f'klucz={key}: {as_text(plain)}')
