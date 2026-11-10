"""Podstawienie: częstości to tylko przybliżenie; popraw mapowanie ręcznie."""
from pathlib import Path
from solvers.classical import substitution, frequency_guess

# DANE
FILE = Path(__file__).resolve().parent.parent / 'tasks' / 'data' / 'encrypted.txt'
TEXT = None   # gdy podasz napis, nie czytamy FILE
MAPPING = None  # np. {'X':'E', 'Q':'T'}; None -> analiza częstości
FREQUENCY = 'ETOAHINSRDLWUFGCBYPMKVJQXZ'

if __name__ == '__main__':
    text = TEXT if TEXT is not None else FILE.read_text(encoding='utf-8')
    if MAPPING is not None:
        print(substitution(text, MAPPING))
    else:
        plain, mapping, counts = frequency_guess(text, FREQUENCY)
        print('Sugestia mapowania:', mapping)
        print(plain)
