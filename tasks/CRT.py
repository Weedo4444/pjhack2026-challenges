'''
The remainder when x is divided by 2305843009213693951 is 95784485401188047.

The remainder when x is divided by 618970019642690137449562111 is 379159085161529952326781.

The remainder when x is divided by 162259276829213363391578010288127 is 379159085161529952326781.

Retrieve x, encode it to hex and then transform it to text to get a flag (FE. with bytes.fromhex(hexValue).decode())
'''

from sympy.ntheory.modular import crt

m = [2305843009213693951, 618970019642690137449562111, 162259276829213363391578010288127]
r = [95784485401188047, 379159085161529952326781, 379159085161529952326781]

x = int(crt(m, r)[0])
print(bytes.fromhex(format(x, 'x')).decode())