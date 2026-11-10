"""S-DES: 10-bitowy klucz (1024 wartości), test znanego prefiksu."""
from solvers.sdes import decrypt_sdes, brute_sdes
from solvers.encoding import as_text

# DANE — skopiuj szyfrogram hex z tasks/S-DES.py
CIPHERTEXT_HEX = ''
KEY = None
PREFIX = b'PJATK{'

if __name__ == '__main__':
    if not CIPHERTEXT_HEX:
        print('Uzupełnij CIPHERTEXT_HEX z tasks/S-DES.py')
    else:
        data = bytes.fromhex(CIPHERTEXT_HEX)
        if KEY is None:
            for key, plain in brute_sdes(data, PREFIX):
                print(f'klucz={key} -> {as_text(plain)}')
        else:
            print(as_text(decrypt_sdes(data, KEY)))
