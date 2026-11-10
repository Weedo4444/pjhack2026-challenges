"""Hash: porównaj wartości dla kandydatów; hash nie jest szyfrem."""
from string import ascii_uppercase
from solvers.hashes import search_hash

# DANE
TARGET = '46a9d7280bedc2c50e40957cf359239d'
TEMPLATE = 'PJATK{char_is_?}'
ALPHABET = ascii_uppercase
ALGORITHM = 'md5'

if __name__ == '__main__':
    print('Znalezione:', search_hash(TARGET, TEMPLATE, ALPHABET, ALGORITHM))
