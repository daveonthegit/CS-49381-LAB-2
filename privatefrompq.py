from sympy import gcd
from Cryptodome.PublicKey import RSA

# Load factored primes from file
factored_primes = {}
with open("factored_primes.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
        key, p_value = lines[i].strip().split(": ")
        _, q_value = lines[i + 1].strip().split(": ")
        factored_primes[key] = (int(p_value), int(q_value))

# Output RSA private keys
output_file = "private_keys.pem"
with open(output_file, "w") as f:
    for key, (p, q) in factored_primes.items():
        n = p * q
        e = 65537
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)  # Compute modular inverse of e mod phi
        
        private_key = RSA.construct((n, e, d, p, q))
        private_pem = private_key.export_key().decode()
        
        f.write(f"# Private key for {key}\n")
        f.write(private_pem + "\n\n")
        
        print(f"Private key for {key} saved.")

print(f"All private keys saved to {output_file}")

