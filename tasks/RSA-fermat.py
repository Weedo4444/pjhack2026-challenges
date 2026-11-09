'''
I have encrypted parts of the flag using RSA and encoded in hex:

"1":0x23b00ce6b0d78615ab6f678a3dc6e659, "2":0xca45835bd5b9b4ad0032eea640da3d0, "3":0x18de627d9a73cc69b627e3528bcbc629, "4":0x1ee72a48869bc3e078caca8d820230fb, "5":0x151e5c01e91e5291a1fb3d04c1cb13f2, "6":0x6f40a51dce867121930dbeb9eff1564,

this is a public key: N = 100000246913740441219878966827008414657 e = 65537
'''


from math import isqrt

N = 100000246913740441219878966827008414657
e = 65537

c = [
    0x23b00ce6b0d78615ab6f678a3dc6e659,
    0xca45835bd5b9b4ad0032eea640da3d0,
    0x18de627d9a73cc69b627e3528bcbc629,
    0x1ee72a48869bc3e078caca8d820230fb,
    0x151e5c01e91e5291a1fb3d04c1cb13f2,
    0x6f40a51dce867121930dbeb9eff1564
]

# Faktoryzacja Fermata
a = isqrt(N) + 1
while isqrt(a*a - N)**2 != a*a - N:
    a += 1

b = isqrt(a*a - N)
p, q = a-b, a+b

# Klucz prywatny
d = pow(e, -1, (p-1)*(q-1))

# Odszyfrowanie flagi
flag = ""
for x in c:
    m = pow(x, d, N)
    flag += m.to_bytes((m.bit_length()+7)//8, "big").decode()

print(flag)
