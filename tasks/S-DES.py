'''
Flag was encrypted with S-DES:

f5 81 83 90 74 7f b9 6c cf 04 75 ab 10 38 e1 77 6a 71 8a 45

Try to decode it knowing that I'm 100% sure that this hex is a flag and i was using 8-bit key
'''



data = bytes.fromhex("f5 81 83 90 74 7f b9 6c cf 04 75 ab 10 38 e1 77 6a 71 8a 45")

P10, P8 = [3,5,2,7,4,10,1,9,8,6], [6,3,7,4,8,5,10,9]
IP, IPI = [2,6,3,1,4,8,5,7], [4,1,3,5,7,2,8,6]
EP, P4 = [4,1,2,3,2,3,4,1], [2,4,3,1]
S = ([[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]],
     [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]])

def perm(x, table, bits):
    return sum(((x >> (bits-i)) & 1) << (len(table)-j-1)
               for j, i in enumerate(table))

def decrypt(c, key):
    x = perm(key, P10, 10)
    a, b = x >> 5, x & 31
    subkeys = []

    for shift in (1, 2):
        a = ((a << shift) | (a >> (5-shift))) & 31
        b = ((b << shift) | (b >> (5-shift))) & 31
        subkeys.append(perm(a << 5 | b, P8, 10))

    x = perm(c, IP, 8)
    for index, k in enumerate(subkeys[::-1]):
        l, r = x >> 4, x & 15
        y = perm(r, EP, 4) ^ k
        z = 0
        for part, box in zip((y >> 4, y & 15), S):
            z = (z << 2) | box[((part & 8) >> 2) | (part & 1)][(part >> 1) & 3]
        l ^= perm(z, P4, 4)
        x = (r << 4 | l) if index == 0 else (l << 4 | r)

    return perm(x, IPI, 8)

for key in range(1024):
    if bytes(decrypt(c, key) for c in data[:5]) == b"PJATK":
        print(key, bytes(decrypt(c, key) for c in data).decode())
