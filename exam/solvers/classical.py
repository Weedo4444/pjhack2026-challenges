"""Szyfry klasyczne; funkcje nie wykonują I/O."""
from collections import Counter
from string import ascii_uppercase


def caesar(text: str, shift: int) -> str:
    result = []
    for c in text:
        base = 65 if 'A' <= c <= 'Z' else 97 if 'a' <= c <= 'z' else None
        result.append(chr((ord(c) - base - shift) % 26 + base) if base else c)
    return ''.join(result)


def caesar_all(text: str, prefix: str = 'PJATK{') -> list[tuple[int, str]]:
    options = [(shift, caesar(text, shift)) for shift in range(26)]
    return sorted(options, key=lambda item: (not item[1].startswith(prefix), item[0]))


def xor_repeat(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError('Pusty klucz XOR')
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def xor_known_prefix(data: bytes, prefix: bytes = b'PJATK{', max_key_length: int = 16):
    """Odzyskaj powtarzany klucz tylko, jeśli znany prefiks ujawnia cały klucz."""
    if max_key_length < 1:
        raise ValueError('max_key_length musi być dodatni')
    found = []
    for n in range(1, min(max_key_length, len(prefix), len(data)) + 1):
        key = bytes(data[i] ^ prefix[i] for i in range(n))
        if xor_repeat(data[:len(prefix)], key) == prefix:
            candidate = xor_repeat(data, key)
            found.append((key, candidate))
    return found


def vigenere(text: str, key: str, decrypt: bool = True) -> str:
    shifts = [ord(c) - 65 for c in key.upper() if c in ascii_uppercase]
    if not shifts:
        raise ValueError('Klucz musi zawierać litery A-Z')
    out, j = [], 0
    for c in text:
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            base = 65 if c.isupper() else 97
            shift = shifts[j % len(shifts)] * (-1 if decrypt else 1)
            out.append(chr((ord(c) - base + shift) % 26 + base))
            j += 1
        else:
            out.append(c)
    return ''.join(out)


def vigenere_recover_key(cipher: str, known_plain: str) -> str:
    """Wyznacza fragment strumienia klucza, NIE automatycznie cały klucz."""
    chars = []
    for c, p in zip(cipher, known_plain):
        if c.upper() in ascii_uppercase and p.upper() in ascii_uppercase:
            chars.append(chr((ord(c.upper()) - ord(p.upper())) % 26 + 65))
    return ''.join(chars)


def substitution(text: str, mapping: dict[str, str]) -> str:
    lookup = {key.upper(): val.upper() for key, val in mapping.items()}
    def replace(c):
        if c.upper() not in lookup:
            return c
        target = lookup[c.upper()]
        return target if c.isupper() else target.lower()
    return ''.join(replace(c) for c in text)


def frequency_guess(text: str, expected: str = 'ETOAHINSRDLWUFGCBYPMKVJQXZ'):
    counts = Counter(c for c in text.upper() if c in ascii_uppercase)
    order = [c for c, _ in counts.most_common()]
    order += [c for c in ascii_uppercase if c not in order]
    mapping = dict(zip(order, expected))
    return substitution(text, mapping), mapping, counts
