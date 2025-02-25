from math import isqrt, ceil

def fermat_factor(n, max_iterations=1000000000):
    a = ceil(isqrt(n))
    b2 = a*a - n
    iterations = 0

    while iterations < max_iterations:
        if b2 >= 0:
            b = isqrt(b2)
            if b * b == b2:
                p = a - b
                q = a + b
                return p, q
        a += 1
        b2 = a*a - n
        iterations += 1

    raise ValueError("Failed to factor within iteration limit.")

# Replace with your formatted modulus
modulus = int("0x00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f", 16)

try:
    p, q = fermat_factor(modulus)
    print(f"[+] Factors found: p = {p}\nq = {q}")
except ValueError as e:
    print(f"[-] {e}")
