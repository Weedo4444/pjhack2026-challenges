"""AES-CBC: wymagany prawidłowy klucz i IV, nie zgaduje klucza."""

def decrypt_aes_cbc(ciphertext: bytes, key: bytes, iv: bytes, unpad: bool = True) -> bytes:
    try:
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import unpad as pkcs7_unpad
    except ImportError as e:
        raise RuntimeError('Zainstaluj: pip install pycryptodome') from e
    if len(key) not in (16, 24, 32) or len(iv) != 16 or len(ciphertext) % 16:
        raise ValueError('Klucz 16/24/32 bajty; IV 16 bajtów; szyfrogram wielokrotność 16')
    plain = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    return pkcs7_unpad(plain, 16) if unpad else plain
