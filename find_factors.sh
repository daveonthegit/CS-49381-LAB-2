#!/bin/bash

# Paths
FASTGCD_PATH="/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/fastgcd/fastgcd"
MODULI_FILE="/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/rsa/1024/output/formatted_moduli.txt"
TEMP_FILE="temp_input.moduli"

# Convert hex to decimal safely
hex_to_dec() {
    cleaned_hex=$(echo "$1" | tr -d '[:space:]' | sed 's/^00*//')
    if [[ -z "$cleaned_hex" ]]; then
        echo "Error: Empty hex value" >&2
        return 1
    fi
    dec=$(echo "ibase=16; ${cleaned_hex^^}" | bc 2>/dev/null)
    if [[ -z "$dec" ]]; then
        echo "Error: Invalid hex input: $cleaned_hex" >&2
        return 1
    fi
    echo "$dec"
}


# Targets
TARGET_MODULUS_1_HEX="00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f"
TARGET_MODULUS_2_HEX="00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"

# Convert target moduli
TARGET_MODULUS_1_DEC=$(hex_to_dec "$TARGET_MODULUS_1_HEX")
TARGET_MODULUS_2_DEC=$(hex_to_dec "$TARGET_MODULUS_2_HEX")

# Calculate q given n and p
calculate_q() {
    echo "$1 / $2" | bc
}

# GCD Check Function
check_gcd_and_factors() {
    local target_dec="$1"
    local mod_hex="$2"
    mod_dec=$(hex_to_dec "$mod_hex")

    # Safety: Check numbers are valid
    [[ -z "$mod_dec" || -z "$target_dec" ]] && return

    # Write to temp file (pure decimals, no spaces)
    printf "%s\n%s" "$target_dec" "$mod_dec" > "$TEMP_FILE"

    # Convert to Unix line endings
    dos2unix "$TEMP_FILE" >/dev/null

    # Run fastgcd
    gcd_output=$("$FASTGCD_PATH" "$TEMP_FILE")

    # Check output validity
    if [[ "$gcd_output" != "No common divisors found." && -n "$gcd_output" ]]; then
        p="$gcd_output"
        q=$(calculate_q "$target_dec" "$p")
        echo "✅ Shared factor found:"
        echo "Modulus: $mod_hex"
        echo "p: $p"
        echo "q: $q"
        echo "-----------------------------------------"
    fi
}

echo "🔍 Starting checks..."

# Process moduli from file
dos2unix "$MODULI_FILE" >/dev/null
while IFS= read -r mod; do
    [[ -z "$mod" ]] && continue
    clean_mod=$(echo "$mod" | tr -d '[:space:]')
    check_gcd_and_factors "$TARGET_MODULUS_1_DEC" "$clean_mod"
    check_gcd_and_factors "$TARGET_MODULUS_2_DEC" "$clean_mod"
done < "$MODULI_FILE"

rm -f "$TEMP_FILE"
echo "✅ Completed."
