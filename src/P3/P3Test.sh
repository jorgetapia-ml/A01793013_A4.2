log_file="word_count_log.txt"
paths=(
    "../../data/P3/TC1.txt"
    "../../data/P3/TC2.txt"
    "../../data/P3/TC3.txt"
    "../../data/P3/TC4.txt"
    "../../data/P3/TC5.txt"

)
> "$log_file"

for path in "${paths[@]}"; do
    echo "Testing with file: $path" | tee -a "$log_file"
    python word_count.py -f "$path" | tee -a "$log_file"
    echo "-----------------------------------" | tee -a "$log_file"
done
echo "-----------------------------------" | tee -a "$log_file"
echo "----------------PyLint-------------------" | tee -a "$log_file"
pylint word_count.py | tee -a "$log_file"
