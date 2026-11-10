"""S-DES: 10-bitowy klucz, Feistel, brute force maks. 1024 klucze."""
P10=[3,5,2,7,4,10,1,9,8,6]
P8=[6,3,7,4,8,5,10,9]
IP=[2,6,3,1,4,8,5,7]
IPI=[4,1,3,5,7,2,8,6]
EP=[4,1,2,3,2,3,4,1]
P4=[2,4,3,1]
S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def _perm(x, table, bits):
    return sum(((x >> (bits-i)) & 1) << (len(table)-j-1) for j,i in enumerate(table))

def _keys(key):
    x = _perm(key, P10, 10)
    l, r = x >> 5, x & 31
    result = []
    for shift in (1,2):
        l = ((l << shift) | (l >> (5-shift))) & 31
        r = ((r << shift) | (r >> (5-shift))) & 31
        result.append(_perm((l << 5)|r, P8, 10))
    return result

def _box(v, box):
    return box[((v & 8) >> 2) | (v & 1)][(v >> 1) & 3]

def decrypt_byte(cipher: int, key: int) -> int:
    if not 0 <= key < 1024:
        raise ValueError('Klucz S-DES 0..1023')
    x = _perm(cipher, IP, 8)
    for round_number, subkey in enumerate(reversed(_keys(key))):
        left, right = x >> 4, x & 15
        mixed = _perm(right, EP, 4) ^ subkey
        value = (_box(mixed >> 4, S0) << 2) | _box(mixed & 15, S1)
        left ^= _perm(value, P4, 4)
        x = (right << 4 | left) if round_number == 0 else (left << 4 | right)
    return _perm(x, IPI, 8)

def decrypt_sdes(data: bytes, key: int) -> bytes:
    return bytes(decrypt_byte(c, key) for c in data)

def brute_sdes(data: bytes, prefix: bytes = b'PJATK{'):
    if len(data) < len(prefix):
        return []
    return [(key, decrypt_sdes(data, key)) for key in range(1024)
            if decrypt_sdes(data[:len(prefix)], key) == prefix]
