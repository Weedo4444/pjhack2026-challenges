# PJHACK 2026 — ściąga do egzaminu z kryptografii

## Szybkie rozpoznawanie

| Charakterystyka | Sugestia| Kluczowa operacja |
|---|---|---|
| ciąg Base64 (`=`, litery/cyfry, `+/`) | kodowanie, nie szyfrowanie | `base64.b64decode` |
| hex (`0-9a-f`) | zapis bajtów; ustal dalszy algorytm | `bytes.fromhex` |
| przesunięte litery, nieznany klucz | Cezar | sprawdź 26 przesunięć |
| znany początek flagi + szyfr z kluczem | known-plaintext attack | porównaj zaszyfrowany i jawny prefiks |
| XOR | `C = P XOR K` | `K = C XOR P` |
| Vigenère | przesunięcia zależne od pozycji | `(C - P) % 26` |
| hashe i krótka niewiadoma | brute force kandydatów | `hashlib` |
| dane AES, klucz, IV | AES-CBC | `decrypt` + `unpad` |
| RSA z `n, e`, czynniki blisko siebie | faktoryzacja Fermata | `n = a² - b²` |
| RSA i klucz prywatny `d` | podpis | `pow(m, d, n)` |
| reszty z dzielenia przez różne moduły | CRT | `crt(moduły, reszty)` |
| ElGamal, mały przedział `x` | brute force wykładnika prywatnego | `b * pow(a, -x, p) % p` |

## 1. [`first_steps.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/first_steps.py) - Base64

**Idea:** tekst zakodowano w Base64. To **kodowanie**, nie szyfrowanie: nie trzeba klucza. Zdekoduj bajty, potem UTF-8.

```python
import base64
encoded = 'UEpBVEt7QmFzaWNfQmFzZTY0fQ=='
print(base64.b64decode(encoded).decode('utf-8'))
```

`.decode()` zamienia bajty na tekst; Base64 → bajty → napis.

## 2. [`simple_ceaser.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/simple_ceaser.py) - Cezar

**Idea:** każda litera jest przesunięta o tę samą liczbę pozycji w alfabecie. Klucz to liczba `0..25`, więc testuj wszystkie możliwości i szukaj `PJATK{`.

```python
cipher = 'AULEV{Zywj_ehpyej_dti_ectpd}'
for k in range(26):
    out = ''
    for c in cipher:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            out += chr((ord(c) - base - k) % 26 + base)
        else:
            out += c
    if out.startswith('PJATK{'):
        print(k, out)
```

**Wzór:** `P = (C - k) mod 26` (litery od `0` do `25`). `% 26` zawija alfabet, symbole `{_}` zostają bez zmian.

## 3. [`XOR.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/XOR.py) - XOR i znany fragment tekstu

**Idea:** `C = P XOR K`, więc również `K = C XOR P`. Znając początek flagi `PJATK`, wylicz pierwszy fragment klucza. W zadaniu powtarza się klucz `OP`.

```python
cipher = bytes.fromhex('1f1a0e04042b3b2510242a2a102a2131220f3c252936262832')
known = b'PJATK'
print(bytes(c ^ p for c, p in zip(cipher, known)))  # fragment klucza
key = b'OP'
plain = bytes(c ^ key[i % len(key)] for i, c in enumerate(cipher))
print(plain.decode())
```

`a ^ b ^ b == a`; dla powtarzanego klucza użyj `i % len(key)`. Nie zakładaj `OP` w innym zadaniu — wyznacz własny klucz z danych.

## 4. [`not_simple_vigenere.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/not_simple_vigenere.py) - Vigenère i znany prefiks

**Idea:** każdy znak przesuwany jest o kolejną literę powtarzanego klucza. Wiemy, że pierwsze 5 liter to `PJATK`, a klucz ma 5 znaków, więc można go odtworzyć z pierwszych 5 liter szyfrogramu.

```python
cipher = 'MQSEN{Mywqlu_dsd_nkvoy_dq_azp_vqhje}'
known = 'PJATK'
key = ''.join(chr((ord(c)-ord(p)) % 26 + 65)
              for c, p in zip(cipher[:5], known))
print('key =', key)
result, i = '', 0
for c in cipher:
    if c.isalpha():
        base = 65 if c.isupper() else 97
        shift = ord(key[i % len(key)]) - 65
        result += chr((ord(c)-base-shift) % 26 + base)
        i += 1
    else:
        result += c
print(result)
```

**Wzory:** `Cᵢ = (Pᵢ + Kᵢ) mod 26`; `Kᵢ = (Cᵢ - Pᵢ) mod 26`. **Uwaga:** w tym skrypcie licznik klucza przesuwa się tylko przy literach; nawiasów i `_` nie liczymy.

## 5. [`substitution_cipher.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/substitution_cipher.py) - podstawienie monoalfabetyczne / częstości

**Idea:** każda litera została zastąpiona stale inną literą. Policz wystąpienia liter w długim szyfrogramie, posortuj od najczęstszej i zestaw z podanym w zadaniu rozkładem `ETOAHINSRDLWUFGCBYPMKVJQXZ`.

```python
from collections import Counter
from pathlib import Path
text = Path('data/encrypted.txt').read_text(encoding='utf-8')
expected = 'ETOAHINSRDLWUFGCBYPMKVJQXZ'
counts = Counter(c for c in text.upper() if c.isalpha())
key = dict(zip([c for c, _ in counts.most_common()], expected))
out = ''.join((key.get(c.upper(), c).upper() if c.isupper()
               else key.get(c.upper(), c).lower()) for c in text)
print(out)
```

To **heurystyka**, nie gwarantowane odwzorowanie. Częstotliwości w skończonym tekście bywają inne: potem koryguj mapowanie, szukając słów i flagi. Potrzebny jest plik `data/encrypted.txt`.

## 6. [`hash.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/hash.py) - hash i mała przestrzeń możliwości

**Idea:** znasz wzór `PJATK{char_is_?}`, a `?` to duża litera `A..Z`. Hash jest jednokierunkowy, ale można policzyć hash **całej kandydackiej flagi** 26 razy i porównać z oczekiwanym.

```python
import hashlib, string
target_md5 = '46a9d7280bedc2c50e40957cf359239d'
for c in string.ascii_uppercase:
    flag = f'PJATK{{char_is_{c}}}'
    if hashlib.md5(flag.encode()).hexdigest() == target_md5:
        print(flag)
```

haszujesz **cały tekst flagi**, nie samą literę. Dla większej pewności porównaj też SHA-1, SHA-256 i SHA-512 (`hashlib.sha256(data).hexdigest()` itd.). Nie „odwracasz” hasha: zgadujesz kandydatów i testujesz.

## 7. [`AES.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/AES.py) - AES-256-CBC

**Idea:** AES to szyfr symetryczny. Masz szyfrogram w Base64, **32-bajtowy klucz** (256 bitów) i **16-bajtowy IV**. Odkoduj Base64, odszyfruj AES-CBC, usuń padding PKCS#7.

```python
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
cipher_b64 = 'MrV6tMNzNODhN6K/BTktHbgl5Nl4ZJacby/zfeVEL7QYpUGW1bc4P2utIQ8EHrsy'
key = b'abcdcbdaeffe21436587098523830cdc'
iv = b'1337337171137331'
raw = base64.b64decode(cipher_b64)
plain = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(raw), 16)
print(plain.decode())
```

Base64 ≠ AES; `iv` ≠ klucz; CBC ma bloki po **16 bajtów** niezależnie od długości klucza. Biblioteka: `pip install pycryptodome`.

## 8. [`S-DES.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/S-DES.py) - uproszczony DES / brute force

**Idea:** dydaktyczny Feistel: permutacje (`P10`, `P8`, `IP`, `IP⁻¹`, `EP`, `P4`), dwa S-boxy, dwie rundy i odwrócona kolejność podkluczy przy deszyfrowaniu. Zaszyfrowany tekst zapisano jako hex. Testujesz wszystkie klucze i sprawdzasz pierwsze bajty flagi.

```python
# Funkcja decrypt(c, key) oraz tablice P10/P8/IP/IPI/EP/P4/S
# są już zaimplementowane w pliku S-DES.py.
for key in range(1024):
    prefix = bytes(decrypt(c, key) for c in data[:5])
    if prefix == b'PJATK':
        print(key, bytes(decrypt(c, key) for c in data).decode())
```

## 9. [`RSA-fermat.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/RSA-fermat.py) - RSA i faktoryzacja Fermata

**Idea:** publiczny klucz `(N, e)`, gdzie `N = p·q`. Gdy `p` i `q` są **blisko siebie**, szukaj `N = a² - b² = (a-b)(a+b)`. Po znalezieniu czynników wylicz prywatny wykładnik `d` i odszyfruj każdy blok.

```python
from math import isqrt
N = 100000246913740441219878966827008414657
e = 65537
# c = [ ... ]  # sześć zaszyfrowanych bloków hex z RSA-fermat.py
a = isqrt(N)
if a*a < N:
    a += 1
while True:
    b2 = a*a - N
    b = isqrt(b2)
    if b*b == b2:
        break
    a += 1
p, q = a-b, a+b
assert p*q == N
d = pow(e, -1, (p-1)*(q-1))
# for x in c:
#     m = pow(x, d, N)
#     print(m.to_bytes((m.bit_length()+7)//8, 'big').decode(), end='')
```

**Wzory:** `φ(N) = (p-1)(q-1)`; `d = e⁻¹ mod φ(N)`; `m = cᵈ mod N`. `pow(e, -1, phi)` oblicza odwrotność modularną, a `pow(c, d, N)` szybkie potęgowanie modularne. **Fermat działa wydajnie przede wszystkim dla bliskich czynników.**

## 10. [`CRT.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/CRT.py) - chińskie twierdzenie o resztach

**Idea:** szukasz liczby `x`, której reszty `x % mᵢ` są znane. CRT składa układ kongruencji w jedno `x` (modulo iloczyn modułów, gdy moduły są parami względnie pierwsze). Potem `x` jest reprezentacją tekstu jako liczby.

```python
from sympy.ntheory.modular import crt
m = [2305843009213693951, 618970019642690137449562111,
     162259276829213363391578010288127]
r = [95784485401188047, 379159085161529952326781,
     379159085161529952326781]
x = int(crt(m, r)[0])
print(bytes.fromhex(format(x, 'x')).decode())
```

`x ≡ rᵢ (mod mᵢ)`; `crt(m, r)[0]` zwraca rozwiązanie. Alternatywnie do konwersji: `x.to_bytes((x.bit_length()+7)//8, 'big').decode()`. Biblioteka: `pip install sympy`.

## 11. [`el_gamal.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/el_gamal.py) - ElGamal i mały zakres klucza

**Idea:** ElGamal szyfruje parą `(a,b)`, gdzie `a = g^k mod p`, `b = m·y^k mod p`, `y = g^x mod p`. Zatem `m = b·(a^x)⁻¹ mod p`. Prywatne `x` leży w zakresie `2100..2200` — testuj tylko 101 wartości.

```python
p = 10007
hex_data = '...'  # pełny długi ciąg z el_gamal.py
numbers = [int(hex_data[i:i+4], 16) for i in range(0, len(hex_data), 4)]
for x in range(2100, 2201):
    out = ''.join(chr(b * pow(a, -x, p) % p)
                  for a, b in zip(numbers[::2], numbers[1::2]))
    if out.startswith('PJATK{'):
        print(x, out)
```

`pow(a, -x, p)` to odwrotność modularna `a^x`. W tym zadaniu każde **4 znaki hex = liczba 16-bitowa**, a kolejne dwie liczby tworzą parę `(a,b)`. Parametr `g=5` nie jest potrzebny do odszyfrowania, jeśli próbujesz `x` bezpośrednio. Wstaw pełne `hex_data` z oryginału.

## 12. [`signature.py`](https://github.com/Weedo4444/pjhack2026-challenges/blob/main/signature.py) - podpis RSA

**Idea:** podpisujesz wiadomość znanym **kluczem prywatnym** `(n,d)`: zamień tekst na liczbę i oblicz `s = m^d mod n`. Wynik zapisz szesnastkowo wewnątrz flagi.

```python
message = 'zolw'
n = 4295229443
d = 2779181297
m = int.from_bytes(message.encode(), 'big')
signature = pow(m, d, n)
print(f'PJATK{{{signature:x}}}')
```

`int.from_bytes(..., 'big')` interpretuje bajty jako liczbę, `:x` formatuje liczbę jako hex bez `0x`. Weryfikacja surowego podpisu: `pow(signature, e, n) == m % n`. **Uwaga:** to ćwiczeniowe *textbook RSA*, a nie bezpieczna procedura podpisu używana w praktyce (tam stosuje się hash i padding, np. RSA-PSS).

---

## Przydatny Python - miniściąga

```python
bytes.fromhex('4142')          # b'AB'
b'AB'.hex()                   # '4142'
int('ff', 16)                 # 255
format(255, 'x')             # 'ff'
ord('A'), chr(65)            # 65, 'A'
text.encode()                # str -> bytes
raw.decode()                 # bytes -> str
pow(7, 11, 13)              # 7**11 % 13 (szybko)
pow(7, -1, 13)              # odwrotność modularna 7 modulo 13
n.to_bytes((n.bit_length()+7)//8, 'big')  # int -> bytes
```
