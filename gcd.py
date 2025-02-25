from math import gcd

# Convert the hex moduli into integers
modulus_1 = int("00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f", 16)
modulus_2 = int("00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7be59ea"
                "ff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5", 16)

# Calculate the greatest common divisor (GCD)
shared_factor = gcd(modulus_1, modulus_2)

# Print the result
if shared_factor != 1:
    print(f"Shared prime factor found: {shared_factor}")
else:
    print("No shared prime factor found.")
