"""Vigenère: K_i = (C_i - P_i) mod 26; pochodny prefiks klucza nie zawsze jest pełnym kluczem."""
from solvers.classical import vigenere, vigenere_recover_key

# DANE
CIPHERTEXT = 'MQSEN{Mywqlu_dsd_nkvoy_dq_azp_vqhje}'
KEY = None     # np. 'ABCDE'; None -> wyprowadź fragment z prefiksu
KNOWN_PLAIN = 'PJATK'
ASSUMED_KEY_LENGTH = 5  # ustaw tylko jeśli treść zadania podaje długość

if __name__ == '__main__':
    recovered = vigenere_recover_key(CIPHERTEXT, KNOWN_PLAIN)
    print('Klucz z prefiksu:', recovered)
    chosen = KEY or (recovered if len(recovered) == ASSUMED_KEY_LENGTH else None)
    if chosen:
        print('Wynik:', vigenere(CIPHERTEXT, chosen))
    else:
        print('Podaj KEY albo prawidłową długość klucza — sam prefiks nie wystarczy.')
