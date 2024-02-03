log_file="compute_statistics_log.txt"
paths=(
    "../data/P1/TC1.txt"
    "../data/P1/TC2.txt"
    "../data/P1/TC3.txt"
    "../data/P1/TC4.txt"
    "../data/P1/TC5.txt"
    "../data/P1/TC6.txt"
    "../data/P1/TC7.txt"
)
> "$log_file"

for path in "${paths[@]}"; do
    echo "Testing with file: $path" | tee -a "$log_file"
    python computeStatistics.py -f "$path" | tee -a "$log_file"
    echo "-----------------------------------" | tee -a "$log_file"
done