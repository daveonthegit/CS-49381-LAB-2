import re

#  Target moduli (hex)
target_moduli_hex = [
    "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f",
    "00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"
]

#  Convert hex to binary
def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:]

target_moduli_bin = [hex_to_bin(h) for h in target_moduli_hex]

#  Read modulus file and convert to binary
def read_moduli(file_path):
    with open(file_path, 'r') as f:
        return [hex_to_bin(match) for match in re.findall(r'([0-9A-Fa-f]+)', f.read())]

moduli_file = "/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/rsa/1024/output/formatted_moduli.txt"
all_moduli_bin = read_moduli(moduli_file)

#  Hamming distance
def hamming_distance(a, b):
    return sum(bit1 != bit2 for bit1, bit2 in zip(a.zfill(len(b)), b.zfill(len(a))))

#  Check for significant bit overlaps
THRESHOLD_PERCENT = 50  # % of bits in common
for target_idx, target in enumerate(target_moduli_bin):
    for idx, modulus in enumerate(all_moduli_bin):
        common_bits = sum(bit1 == bit2 for bit1, bit2 in zip(target, modulus))
        overlap_percent = (common_bits / len(target)) * 100
        if overlap_percent >= THRESHOLD_PERCENT:
            print(f" Modulus #{idx+1} shares {overlap_percent:.2f}% bits with Target #{target_idx+1}!")


