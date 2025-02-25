#!/bin/bash

# Input and output file paths
input_file="/mnt/c/Users/darkf/Documents/CSCI-Work-main/CS-49381-LAB-2/rsa/1024/output/modulus_output_2.txt"
output_file="formatted_moduli.txt"

# Extract modulus lines, remove "Modulus=" label, and save them
grep "Modulus=" "$input_file" | sed 's/Modulus=//' > "$output_file"

echo "Formatted moduli saved to $output_file"
