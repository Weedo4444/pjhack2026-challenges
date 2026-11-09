'''
I’ve lost the key to this simple Vigenère cipher again:

MQSEN{Mywqlu_dsd_nkvoy_dq_azp_vqhje}

All I remember is that the key was 5 characters long and that it is definitely a flag. Good luck!
'''

encrypted = "MQSEN{Mywqlu_dsd_nkvoy_dq_azp_vqhje}"
known = "PJATK" # znany element flagi

# Odzyskujemy 5-literowy klucz
key = ""

for c, p in zip(encrypted[:5], known): # biorę pierwsze 5 znaków z encrypted i porównuję je z known (flaga)
    shift = (ord(c) - ord(p)) % 26
    key += chr(shift + ord("A"))

print("Klucz:", key)

# Odszyfrowujemy flagę
result = ""
i = 0

for char in encrypted:
    if char.isalpha():
        base = ord("A") if char.isupper() else ord("a")
        shift = ord(key[i % len(key)]) - ord("A")
        result += chr((ord(char) - base - shift) % 26 + base)
        i += 1
    else:
        result += char

print("Flaga:", result)
