"""XOR: P = C XOR K, a znajomy prefiks umożliwia odzyskanie krótkiego klucza."""
from solvers.classical import xor_repeat, xor_known_prefix
from solvers.encoding import as_text

# DANE
CIPHERTEXT_HEX = '1f1a0e04042b3b2510242a2a102a2131220f3c252936262832'
KEY = None        # None -> szukaj klucza; albo np. b'OP'
PREFIX = b'PJATK{'
MAX_KEY_LENGTH = 12

if __name__ == '__main__':
    binary = bytes.fromhex(CIPHERTEXT_HEX)
    if KEY is not None:
        print(as_text(xor_repeat(binary, KEY)))
    else:
        for key, result in xor_known_prefix(binary, PREFIX, MAX_KEY_LENGTH):
            print(f'klucz={key!r} (hex={key.hex()}) -> {as_text(result)}')
