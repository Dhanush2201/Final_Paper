# Rabin-Karp Algorithm
def rabin_karp(pattern, text):
    occurrences = []
    m = len(pattern)
    n = len(text)
    pattern_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i+m]) == pattern_hash:
            if text[i:i+m] == pattern:
                occurrences.append(i)
    return occurrences

def benchmark_rabin_karp(pattern, text):
    return timeit.timeit(lambda: rabin_karp(pattern, text), number=10)

def rabin_karp_benchmarks(input_sizes):
    all_runtimes_best = []
    all_runtimes_worst = []
    all_runtimes_average = []

    for pattern_length, text_length in input_sizes:
        best_case_pattern, best_case_text, worst_case_pattern, worst_case_text, average_case_pattern, average_case_text = generate_test_cases(pattern_length, text_length)
        
        runtime_best = benchmark_rabin_karp(best_case_pattern, best_case_text)
        runtime_worst = benchmark_rabin_karp(worst_case_pattern, worst_case_text)
        runtime_average = benchmark_rabin_karp(average_case_pattern, average_case_text)
        
        all_runtimes_best.append(runtime_best)
        all_runtimes_worst.append(runtime_worst)
        all_runtimes_average.append(runtime_average)

    return all_runtimes_best, all_runtimes_worst, all_runtimes_average

# Input sizes to test
input_sizes = [(5, 100), (10, 200), (20, 400), (50, 1000), (100, 2000)]

# Benchmarking for Rabin-Karp Algorithm
algorithm_runtimes_best, algorithm_runtimes_worst, algorithm_runtimes_average = rabin_karp_benchmarks(input_sizes)

plt.figure(figsize=(10, 6))

# Plot best-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_best, label='Best Case')

# Plot worst-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_worst, label='Worst Case')

# Plot average-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_average, label='Average Case')

plt.xlabel('Text Length')
plt.ylabel('Runtime (seconds)')
plt.title('Rabin-Karp Algorithm Runtimes')
plt.legend()
plt.grid(True)
plt.show()
