import math

# Extracted modulus from the certificate (in hex)
certificate_modulus_hex = "C43CDA0AC84DA932205AEB7249969F5C5F3859D337573D6799118B4E5ADAC50DC67FF743CD36F25F560055F8E2CA424A0E09FCC1A94A4441AC793F8ED1E06A38645AFE3E7A1D2A731A278CE79D2233F19BDD431F964F14F7A6F7C4AB700BA13C67B21E4C2314E91151B0B6454A8412968841DB33E576D2BD93C7E707821CD19F877F1A248153B1CFA79B3FFF5AD05E98993698F115B3227000BFD719DAD63355F45357811BC6731235516189B8D8C92E0F20B7DC6382F7A7D9A1CFB31B8DA89758F0D00253A6783650CCF26C3633A8C7BD658FC072E66EB470D6A5F8ED02F35BEE3CE561F518131285700AAD758AA136592BC17C4A414F4B99BAAAB5876616EF"

# Convert to integer
certificate_modulus = int(certificate_modulus_hex, 16)

# Target moduli (replace with actual ones if different)
target_moduli_hex = [
    "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f",
    "00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"
]

# Convert target moduli to integers
target_moduli = [int(mod, 16) for mod in target_moduli_hex]

# Check for shared factors
for idx, target in enumerate(target_moduli, 1):
    gcd = math.gcd(certificate_modulus, target)
    if 1 < gcd < certificate_modulus:
        q = certificate_modulus // gcd
        print(f"✅ Shared factor found with Target #{idx}:")
        print(f"p (shared factor): {gcd}")
        print(f"q (other factor): {q}")
    else:
        print(f"❌ No shared factor with Target #{idx}.")
