# Knuth-Morris-Pratt Algorithm
def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

def knuth_morris_pratt(pattern, text):
    occurrences = []
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences

def benchmark_knuth_morris_pratt(pattern, text):
    return timeit.timeit(lambda: knuth_morris_pratt(pattern, text), number=10)

def knuth_morris_pratt_benchmarks(input_sizes):
    all_runtimes_best = []
    all_runtimes_worst = []
    all_runtimes_average = []

    for pattern_length, text_length in input_sizes:
        best_case_pattern, best_case_text, worst_case_pattern, worst_case_text, average_case_pattern, average_case_text = generate_test_cases(pattern_length, text_length)
        
        runtime_best = benchmark_knuth_morris_pratt(best_case_pattern, best_case_text)
        runtime_worst = benchmark_knuth_morris_pratt(worst_case_pattern, worst_case_text)
        runtime_average = benchmark_knuth_morris_pratt(average_case_pattern, average_case_text)
        
        all_runtimes_best.append(runtime_best)
        all_runtimes_worst.append(runtime_worst)
        all_runtimes_average.append(runtime_average)

    return all_runtimes_best, all_runtimes_worst, all_runtimes_average

# Input sizes to test
input_sizes = [(5, 100), (10, 200), (20, 400), (50, 1000), (100, 2000)]

# Benchmarking for Knuth-Morris-Pratt Algorithm
algorithm_runtimes_best, algorithm_runtimes_worst, algorithm_runtimes_average = knuth_morris_pratt_benchmarks(input_sizes)

plt.figure(figsize=(10, 6))

# Plot best-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_best, label='Best Case')

# Plot worst-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_worst, label='Worst Case')

# Plot average-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_average, label='Average Case')

plt.xlabel('Text Length')
plt.ylabel('Runtime (seconds)')
plt.title('Knuth-Morris-Pratt Algorithm Runtimes')
plt.legend()
plt.grid(True)
plt.show()
