"""Base64: kodowanie, nie szyfrowanie. Zmieniaj sekcję DANE."""
from solvers.encoding import decode_base64, as_text

# DANE
CIPHERTEXT = 'UEpBVEt7QmFzaWNfQmFzZTY0fQ=='

if __name__ == '__main__':
    print(as_text(decode_base64(CIPHERTEXT)))
