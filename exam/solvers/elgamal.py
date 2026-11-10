"""ElGamal z małym zakresem prywatnego wykładnika (ćwiczeniowy)."""

def parse_pairs(hex_data: str, word_chars: int = 4) -> list[tuple[int, int]]:
    data = ''.join(hex_data.split())
    if word_chars < 1 or len(data) % (2*word_chars):
        raise ValueError('Każda para musi mieć dwa słowa hex')
    values = [int(data[i:i+word_chars], 16) for i in range(0, len(data), word_chars)]
    return list(zip(values[::2], values[1::2]))


def decrypt_elgamal(p: int, pairs: list[tuple[int, int]], x: int) -> list[int]:
    return [(b * pow(a, -x, p)) % p for a, b in pairs]


def search_elgamal(p: int, pairs: list[tuple[int, int]], start: int, end: int,
                   prefix: bytes = b'PJATK{'):
    if end < start or end-start > 100000:
        raise ValueError('Nieprawidłowy zakres')
    results = []
    for x in range(start, end+1):
        nums = decrypt_elgamal(p, pairs, x)
        if all(0 <= n < 256 for n in nums):
            plain = bytes(nums)
            if plain.startswith(prefix):
                results.append((x, plain))
    return results
