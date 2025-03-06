#!/bin/bash

# Output file for extracted moduli
OUTPUT_FILE="1024_bit_moduli.txt"
> "$OUTPUT_FILE"  # Clear the file before writing

# Loop through all extracted certificates
for cert in cert_*.pem; do
    echo "Checking key size for $cert..."
    
    # Extract the public key size
    KEY_SIZE=$(openssl x509 -in "$cert" -text -noout | grep "Public-Key" | awk '{print $2}')
    
    # If the key is 1024 bits, extract the modulus
    if [[ "$KEY_SIZE" == "(1024" ]]; then
        echo "Extracting modulus for $cert..."
        MODULUS=$(openssl x509 -in "$cert" -noout -modulus | awk -F'=' '{print $2}')
        echo "Modulus for $cert: $MODULUS" | tee -a "$OUTPUT_FILE"
    fi
done

# Print completion message
echo "Extraction complete. 1024-bit moduli saved in $OUTPUT_FILE"
