import logging
from datetime import datetime
import gmpy2
import re

#  Setup logging
log_filename = "gcd_shared_primes.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename, mode="w"),
        logging.StreamHandler()
    ]
)

def log_and_print(message):
    """Helper to log and print simultaneously."""
    logging.info(message)

#  Load moduli from file
def load_moduli(file_path):
    moduli = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and re.match(r"^[0-9A-Fa-f]+$", line):
                    moduli.append(int(line, 16))
        log_and_print(f" Loaded {len(moduli)} moduli from '{file_path}'.")
    except Exception as e:
        log_and_print(f" Error loading moduli: {e}")
    return moduli

#  Check for shared prime factors using GCD
def check_shared_primes(target_modulus, moduli_list):
    found = False
    for idx, modulus in enumerate(moduli_list, start=1):
        gcd = gmpy2.gcd(target_modulus, modulus)
        if gcd > 1 and gcd != target_modulus and gcd != modulus:
            p = gcd
            q = target_modulus // p
            log_and_print(f" Shared prime factor found with modulus #{idx}:")
            log_and_print(f"  p: {p}")
            log_and_print(f"  q: {q}")
            found = True
    if not found:
        log_and_print(" No shared primes found.")

#  Example usage
if __name__ == "__main__":
    #  Target modulus (replace with actual)
    target_modulus_hex = "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f"
    n_target = int(target_modulus_hex, 16)

    #  Moduli file path (use raw string or forward slashes)
    moduli_file = "/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/rsa/1024/output/formatted_moduli.txt"


    log_and_print(" Starting GCD shared prime check...")
    all_moduli = load_moduli(moduli_file)
    check_shared_primes(n_target, all_moduli)
    log_and_print(" Process completed.")

