"""CRT: x % mi == ri, potem wynik x zamieniamy na bajty."""
from solvers.crt import solve_crt
from solvers.encoding import int_bytes, as_text

# DANE
MODULI = [2305843009213693951, 618970019642690137449562111, 162259276829213363391578010288127]
RESIDUES = [95784485401188047, 379159085161529952326781, 379159085161529952326781]

if __name__ == '__main__':
    x, modulus = solve_crt(MODULI, RESIDUES)
    print('x:', x, 'modulo:', modulus)
    print('Tekst:', as_text(int_bytes(x)))
