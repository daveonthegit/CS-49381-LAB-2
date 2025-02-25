import gmpy2
import re

# 📝 Target moduli (hex -> int)
target_moduli = [
    int("00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f", 16),
    int("00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5", 16)
]

# 📂 Read moduli from file
def read_moduli(file_path):
    try:
        with open(file_path, 'r') as f:
            moduli = re.findall(r'Modulus=([0-9A-Fa-f]+)', f.read())
            if not moduli:
                print("⚠️ No moduli found. Check file format.")
            return [int(mod, 16) for mod in moduli]
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []

# 🔎 Check for shared factors
def check_shared_factors(targets, moduli_list):
    found = False
    for t_idx, target in enumerate(targets):
        for idx, modulus in enumerate(moduli_list):
            gcd = gmpy2.gcd(target, modulus)
            if gcd > 1 and gcd != target and gcd != modulus:
                q = target // gcd
                found = True
                print(f"\n✅ Shared factor found!")
                print(f"🔑 Modulus #{idx + 1} & Target #{t_idx + 1}")
                print(f"p: {gcd}\nq: {q}\n{'-'*40}")
    if not found:
        print("❌ No shared factors detected.")

# 📄 Path to your moduli output file
modulus_output_file = "/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/rsa/1024/output/modulus_output_3.txt"

print("🔍 Checking for shared factors...")
all_moduli = read_moduli(modulus_output_file)
if all_moduli:
    check_shared_factors(target_moduli, all_moduli)
