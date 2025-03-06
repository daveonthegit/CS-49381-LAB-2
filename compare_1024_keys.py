from sympy import gcd

# Given 1024-bit keys in hexadecimal
N1_HEX = "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f"
N2_HEX = "00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7beebe59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"

# Convert to decimal
N1_DEC = int(N1_HEX, 16)
N2_DEC = int(N2_HEX, 16)

# Load extracted 1024-bit moduli from file
moduli = {}
with open("1024_bit_moduli.txt", "r") as f:
    for line in f:
        if "Modulus for" in line:
            parts = line.strip().split(": ")
            cert_name = parts[0].split(" ")[2]
            modulus_hex = parts[1]
            moduli[cert_name] = int(modulus_hex, 16)

# Compare each extracted modulus against the given keys
output_file = "gcd_comparison_results.txt"
with open(output_file, "w") as f:
    for cert, modulus in moduli.items():
        gcd_n1 = gcd(modulus, N1_DEC)
        gcd_n2 = gcd(modulus, N2_DEC)
        
        f.write(f"GCD({cert}, N1): {gcd_n1}\n")
        f.write(f"GCD({cert}, N2): {gcd_n2}\n")
        print(f"GCD({cert}, N1): {gcd_n1}")
        print(f"GCD({cert}, N2): {gcd_n2}")

print(f"Comparison complete. Results saved to {output_file}")
