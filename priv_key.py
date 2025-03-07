from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

# Replace with your actual primes
p = 475
q = 62174433086242002786739388778318766855503164371033237297091548088619079166806048196292798559841633479449605282696319101014568517226249912020116002125724400483528868247980427821308028544493481144953850838631315796120233929750582229787374127379232128603814981359150660987731949108200598614873522437792909044957
e = 65537

# Calculate modulus and totient
n = p * q
phi = (p - 1) * (q - 1)

# Compute private exponent d
d = inverse(e, phi)

# Generate RSA private key
key = RSA.construct((n, e, d, p, q))

# Export the private key in PEM format
with open("reconstructed_key.pem", "wb") as f:
    f.write(key.export_key())
print("✅ RSA private key saved as reconstructed_key.pem")

