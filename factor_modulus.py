import gmpy2
from gmpy2 import mpz, isqrt, gcd, powmod, is_prime
from multiprocessing import Pool, cpu_count

#  Input modulus (replace with your actual modulus)
MODULUS_HEX = "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f"
n = mpz(int(MODULUS_HEX, 16))


def validate_factors(p, q, n):
    """ Check if p and q are valid prime factors of n."""
    return p * q == n and is_prime(p) and is_prime(q)


#  Pollard's Rho Factorization with Validation
def pollards_rho(n, seed=2):
    if n % 2 == 0:
        return 2
    x, y, d = mpz(seed), mpz(seed), mpz(1)
    f = lambda x: (powmod(x, 2, n) + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d if 1 < d < n else None


#  Parallel Pollard’s Rho with Result Filtering
def parallel_pollards_rho(n):
    seeds = list(range(2, 2 + cpu_count()))  # Try seeds for parallelism
    with Pool() as pool:
        candidates = pool.starmap(pollards_rho, [(n, seed) for seed in seeds])

    #  Validate results
    for p in candidates:
        if p:
            q = n // p
            if validate_factors(p, q, n):
                return p, q
    return None, None


#  Factor using fallback methods
def factor_modulus(n):
    print("🔍 Attempting Pollard’s Rho...")
    p, q = parallel_pollards_rho(n)
    if p and q:
        print(f" Valid Factors Found:\np: {p}\nq: {q}")
        return p, q
    else:
        print(" Pollard’s Rho failed or found invalid factors.")
        return None, None


#  Run factorization
p, q = factor_modulus(n)
if not p:
    print(" Consider using CADO-NFS or a known weak key approach.")

