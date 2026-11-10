"""AES-CBC: Base64 -> bajty -> AES-CBC -> zdjęcie paddingu PKCS#7."""
from solvers.encoding import decode_base64, as_text
from solvers.aes import decrypt_aes_cbc

# DANE (klucz i IV to BAJTY, nie zapis hex)
CIPHERTEXT_BASE64 = 'MrV6tMNzNODhN6K/BTktHbgl5Nl4ZJacby/zfeVEL7QYpUGW1bc4P2utIQ8EHrsy'
KEY = b'abcdcbdaeffe21436587098523830cdc'
IV = b'1337337171137331'

if __name__ == '__main__':
    print(as_text(decrypt_aes_cbc(decode_base64(CIPHERTEXT_BASE64), KEY, IV)))
