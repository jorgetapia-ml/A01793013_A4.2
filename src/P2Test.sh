log_file="convert_numbers_log.txt"
paths=(
    "../data/P2/TC1.txt"
    "../data/P2/TC2.txt"
    "../data/P2/TC3.txt"
    "../data/P2/TC4.txt"

)
> "$log_file"

for path in "${paths[@]}"; do
    echo "Testing with file: $path" | tee -a "$log_file"
    python convertNumbers.py -f "$path" | tee -a "$log_file"
    echo "-----------------------------------" | tee -a "$log_file"
done