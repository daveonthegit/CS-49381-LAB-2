import math
import re

# Paste your target moduli (hex format, without spaces or colons)
target_moduli = [
    "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f",
    "00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee5959ea ff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"
]

# Clean target moduli and convert to integers
target_moduli = [int(modulus.replace(" ", "").replace("\n", "").replace(":", ""), 16) for modulus in target_moduli]

# Read extracted moduli from your output files
def read_moduli_from_file(file_path):
    moduli = []
    with open(file_path, 'r') as file:
        content = file.read()
        # Regex to find modulus lines (MODULUS=hex OR Modulus=hex)
        matches = re.findall(r'Modulus=([0-9A-Fa-f]+)', content)
        for match in matches:
            moduli.append(int(match, 16))
    return moduli

# Replace with your actual modulus output file path
modulus_output_files = ["modulus_output_2.txt"]

# Read all moduli from extracted files
all_moduli = []
for file_path in modulus_output_files:
    all_moduli.extend(read_moduli_from_file(file_path))

# Check for shared prime factors using GCD
def check_shared_factors(targets, moduli_list):
    for target_idx, target in enumerate(targets):
        for idx, modulus in enumerate(moduli_list):
            gcd = math.gcd(target, modulus)
            if gcd != 1 and gcd != target and gcd != modulus:
                print(f"[!] Shared factor found with modulus #{idx + 1} and target #{target_idx + 1}:")
                print(f"    Shared Prime (p): {gcd}")
                print(f"    Other Prime (q): {target // gcd}")
                print()

check_shared_factors(target_moduli, all_moduli)
