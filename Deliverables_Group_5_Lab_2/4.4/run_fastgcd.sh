#!/bin/bash

# 🛠️ Paths
FASTGCD_PATH="/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/fastgcd/fastgcd"
MODULI_FILE="/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/rsa/1024/output/formatted_moduli.txt"
OUTPUT_FILE="fastgcd_results.txt"
TEMP_FILE="temp_input.moduli"

# 🧹 Clean previous output
echo "🔍 FastGCD Results" > "$OUTPUT_FILE"
echo "==================" >> "$OUTPUT_FILE"

# 🎯 Target moduli (hex)
TARGET_MODULI_HEX=(
    "00a4482ebb0580823df76ce4ebbc259c45bfdb51ac75eca9e8e372fc7c7cbdbdf5ea2415d5e7de75b67ac4107f83738626674e46253af960ea0f2bcbfe1c45e33fe5725f549433fc384846ec16976acf42982de811af301010e9bc0bc12405e742515f01074da2e8cb4015a74b0a57947d2a3f3fd0c2b50246dad7ca9c4b7c763e0f"
    "00a7379c4c73718c01c5215a1fb7b61a183d0f4480d2d1f3a4d77f310ded7ccd27c93bacf5214383e674dc30dfa0f644151c72bc265558c30cc4789e7bee59eaff19a4f49378343893222cac752ec2ca240f6e99813145057cf94c27ff19b1f52323bba7f52b4400cf1db57bf05666f11931eca95610106ea3fce3a306a89de5"
)

# 🔄 Convert hex to decimal
hex_to_dec() {
    local hex_value="${1// /}"
    hex_value="${hex_value//[^0-9A-Fa-f]/}"
    echo "ibase=16; ${hex_value^^}" | bc
}

# 🧮 Calculate q given n and p
calculate_q() {
    echo "$(( $1 / $2 ))"
}

# 🚀 Run FastGCD and process results
run_fastgcd() {
    local target_dec="$1"
    local mod_dec="$2"
    local line_num="$3"

    # 📝 Write decimal moduli to temp file
    printf "%s\n%s\n" "$target_dec" "$mod_dec" > "$TEMP_FILE"
    dos2unix "$TEMP_FILE" >/dev/null

    # 🏎️ Run fastgcd
    gcd_output=$("$FASTGCD_PATH" "$TEMP_FILE" 2>/dev/null)

    # 🔑 Check and display results
    if [[ -n "$gcd_output" && "$gcd_output" != "No common divisors found." ]]; then
        p="$gcd_output"
        q=$(calculate_q "$target_dec" "$p")
        echo "✅ [Line $line_num] Shared factor found:" | tee -a "$OUTPUT_FILE"
        echo "p: $p" | tee -a "$OUTPUT_FILE"
        echo "q: $q" | tee -a "$OUTPUT_FILE"
        echo "-----------------------------------------" | tee -a "$OUTPUT_FILE"
    else
        echo "❌ [Line $line_num] No shared factors found." | tee -a "$OUTPUT_FILE"
    fi
}

echo "🔍 Starting FastGCD checks..."
echo "" >> "$OUTPUT_FILE"

# 🛠️ Convert target moduli to decimal
TARGET_MODULI_DEC=()
for hex in "${TARGET_MODULI_HEX[@]}"; do
    dec=$(hex_to_dec "$hex")
    TARGET_MODULI_DEC+=("$dec")
done

# 📂 Process moduli from file
dos2unix "$MODULI_FILE" >/dev/null
line_number=1
while IFS= read -r mod_hex; do
    [[ -z "$mod_hex" ]] && { ((line_number++)); continue; }

    mod_dec=$(hex_to_dec "$mod_hex")
    if [[ -z "$mod_dec" ]]; then
        echo "⚠️ [Line $line_number] Invalid hex format. Skipping." | tee -a "$OUTPUT_FILE"
        ((line_number++))
        continue
    fi

    # 🔎 Check both target moduli
    for target_idx in "${!TARGET_MODULI_DEC[@]}"; do
        echo "🔎 Checking modulus on line $line_number against Target $((target_idx + 1))..." >> "$OUTPUT_FILE"
        run_fastgcd "${TARGET_MODULI_DEC[$target_idx]}" "$mod_dec" "$line_number"
    done

    ((line_number++))
done < "$MODULI_FILE"

# 🧹 Cleanup
rm -f "$TEMP_FILE"
echo "✅ FastGCD checks completed. Results saved to $OUTPUT_FILE."
