"""Słownikowe testowanie małej przestrzeni kandydatów — nie odwracanie hasha."""
import hashlib


def search_hash(target: str, template: str, alphabet: str, algorithm: str = 'md5') -> list[str]:
    if template.count('?') != 1:
        raise ValueError('W szablonie ma wystąpić dokładnie jedno ?')
    if len(alphabet) > 100000:
        raise ValueError('Zbyt duży alfabet')
    hashlib.new(algorithm)  # sprawdź nazwę
    result = []
    for char in alphabet:
        candidate = template.replace('?', char)
        if hashlib.new(algorithm, candidate.encode()).hexdigest().lower() == target.lower():
            result.append(candidate)
    return result
