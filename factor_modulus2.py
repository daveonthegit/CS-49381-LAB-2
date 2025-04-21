import gmpy2
from gmpy2 import mpz, isqrt, gcd, powmod, is_square
from multiprocessing import Pool, cpu_count

# 📥 Input modulus (replace with your actual modulus)
MODULUS_HEX = "00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"
n = mpz(int(MODULUS_HEX, 16))

# 🧮 Pollard's Rho Factorization
def pollards_rho(n, seed=2):
    if n % 2 == 0:
        return 2
    x, y, d = mpz(seed), mpz(seed), mpz(1)
    f = lambda x: (powmod(x, 2, n) + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d if d != n else None

# 🧮 Fermat’s Factorization (Optimized with gmpy2)
def fermat_factor(n):
    a = isqrt(n) + 1
    b2 = a * a - n
    while not is_square(b2):
        a += 1
        b2 = a * a - n
    b = isqrt(b2)
    return a - b, a + b

# 🏎️ Parallel Pollard’s Rho across multiple cores
def parallel_pollards_rho(n):
    seeds = list(range(2, 2 + cpu_count()))  # Different seeds for parallel runs
    with Pool() as pool:
        results = pool.starmap(pollards_rho, [(n, seed) for seed in seeds])
    return next((res for res in results if res and res != n), None)

# 🚀 Run factorization attempts
def factor_modulus(n):
    print("🔍 Attempting Pollard’s Rho...")
    p = parallel_pollards_rho(n)
    if p:
        q = n // p
        print(f"✅ Factors found with Pollard’s Rho:\np: {p}\nq: {q}")
        return p, q

    print("⚠️ Pollard’s Rho failed. Trying Fermat’s Method...")
    p, q = fermat_factor(n)
    print(f"✅ Factors found with Fermat’s Method:\np: {p}\nq: {q}")
    return p, q

# 🚦 Run the factorization
p, q = factor_modulus(n)

