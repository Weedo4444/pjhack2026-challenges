'''
See this:

AULEV{Zywj_ehpyej_dti_ectpd}

I forgot to save key, try find it and decipher it!
'''

encrypted = "AULEV{Zywj_ehpyej_dti_ectpd}"

decoded = ""

for key in range(1, 26):
    for c in encrypted:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            decoded += chr((ord(c) - base - key) % 26 + base)
        else:
            decoded += c
    print(decoded)
    decoded = ""