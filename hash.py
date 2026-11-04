'''
the flag IS NOT PJATK{char_is_?} : instead od ? it has an Uppercase letter. Hash of this flag is:

MD5 46a9d7280bedc2c50e40957cf359239d

SHA1 e8f3b58ca21ff9d066e1327a55b7ee53f4df395b

SHA-256 8f27ddee069a7e91853099ba1f26a7565c4548dd5fb5234d232c323c79e27d7d

SHA-512 9e45d4469629710ea053f68e3e7c9a6045bbfef264698ddedd1ff8adc7f116ebca5cf70a4e29d0d32f1763f6fd856325f6a693d78368edebd5ae044e18511d9e

Fe. if it is with letter A, a flag is PJATK{char_is_A} because hash md5 of the flag is 5d9c9ee79ab0faa538522df0677bbabb (NOT the hash of letter A) You have only 4 tries
'''


import hashlib
import string

# słownik hashy
hashes = {
    "md5": "46a9d7280bedc2c50e40957cf359239d",
    "sha1": "e8f3b58ca21ff9d066e1327a55b7ee53f4df395b",
    "sha256": "8f27ddee069a7e91853099ba1f26a7565c4548dd5fb5234d232c323c79e27d7d",
    "sha512": "9e45d4469629710ea053f68e3e7c9a6045bbfef264698ddedd1ff8adc7f116ebca5cf70a4e29d0d32f1763f6fd856325f6a693d78368edebd5ae044e18511d9e"
}

# Sprawdzamy wszystkie wielkie litery od A do Z
for letter in string.ascii_uppercase:

    # Tworzymy flagę z aktualną literą, np. PJATK{char_is_A}
    flag = f"PJATK{{char_is_{letter}}}"

    # Zamieniamy tekst flagi na bajty
    data = flag.encode()

    # Sprawdzamy, czy wszystkie 4 hashe pasują do podanych
    if all(
        getattr(hashlib, name)(data).hexdigest() == target
        for name, target in hashes.items()
    ):
        # Jeśli wszystkie pasują, wypisujemy flagę
        print(flag)
        break  # Kończymy szukanie
