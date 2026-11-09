'''
This long text was encrypted with substitution cipher Only thing I know is that this string of letter is sorted from most common to least common (from left to right)

ETOAHINSRDLWUFGCBYPMKVJQXZ

Find a flag and decrypt it
'''


from collections import Counter
from pathlib import Path

text = Path("data/encrypted.txt").read_text(encoding="utf-8")

freq = "ETOAHINSRDLWUFGCBYPMKVJQXZ"
letters = Counter(c for c in text.upper() if c.isalpha())
sorted_letters = [c for c, _ in letters.most_common()]

key = dict(zip(sorted_letters, freq))

decoded = "".join(
    key.get(c.upper(), c) if c.isupper() else key.get(c.upper(), c).lower()
    for c in text
)

print(decoded)


