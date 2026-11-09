'''
This flag was written in hexadecimal and used with XOR:

1f1a0e04042b3b2510242a2a102a2131220f3c252936262832

Sadly, again I've lost the key but I am sure this is a flag
'''

cipher_hex = "1f1a0e04042b3b2510242a2a102a2131220f3c252936262832"

# HEX -> bajty
cipher = bytes.fromhex(cipher_hex)
print(cipher)

# Znamy początek flagi
known = b"PJATK"

# Odzyskanie pierwszych bajtów klucza
key_fragment = bytes(
    c ^ p for c, p in zip(cipher, known)
)

print("Odzyskany fragment klucza:", key_fragment)

# Rozpoznaliśmy powtarzający się klucz OP
key = b"OP"

# XOR z powtarzanym kluczem
plaintext = bytes(
    c ^ key[i % len(key)]
    for i, c in enumerate(cipher)
)

print("Flaga:", plaintext.decode())
