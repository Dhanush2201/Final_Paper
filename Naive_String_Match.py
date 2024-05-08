import timeit
import random
import matplotlib.pyplot as plt

# Naive String Matching Algorithm
def naive_string_match(pattern, text):
    occurrences = []
    m = len(pattern)
    n = len(text)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)
    return occurrences

def benchmark_naive_string_match(pattern, text):
    return timeit.timeit(lambda: naive_string_match(pattern, text), number=10)

# Generate test cases
def generate_test_cases(pattern_length, text_length):
    # Best-case scenario: pattern appears at the beginning of the text
    best_case_pattern = "a" * pattern_length
    best_case_text = best_case_pattern + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=text_length - pattern_length))
    
    # Worst-case scenario: pattern does not appear in the text
    worst_case_pattern = "a" * pattern_length
    worst_case_text = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=text_length))

    # Average-case scenario: pattern appears randomly in the text
    average_case_pattern = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=pattern_length))
    average_case_text = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=text_length))

    return best_case_pattern, best_case_text, worst_case_pattern, worst_case_text, average_case_pattern, average_case_text

# Benchmarking for a given algorithm and test cases
def string_matching_benchmarks(algorithm, input_sizes):
    all_runtimes_best = []
    all_runtimes_worst = []
    all_runtimes_average = []

    for pattern_length, text_length in input_sizes:
        best_case_pattern, best_case_text, worst_case_pattern, worst_case_text, average_case_pattern, average_case_text = generate_test_cases(pattern_length, text_length)
        
        runtime_best = benchmark_naive_string_match(best_case_pattern, best_case_text)
        runtime_worst = benchmark_naive_string_match(worst_case_pattern, worst_case_text)
        runtime_average = benchmark_naive_string_match(average_case_pattern, average_case_text)
        
        all_runtimes_best.append(runtime_best)
        all_runtimes_worst.append(runtime_worst)
        all_runtimes_average.append(runtime_average)

    return all_runtimes_best, all_runtimes_worst, all_runtimes_average

# Input sizes to test
input_sizes = [(5, 100), (10, 200), (20, 400), (50, 1000), (100, 2000)]

# Benchmarking for Naive String Matching
algorithm_runtimes_best, algorithm_runtimes_worst, algorithm_runtimes_average = string_matching_benchmarks(naive_string_match, input_sizes)

plt.figure(figsize=(10, 6))

# Plot best-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_best, label='Best Case')

# Plot worst-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_worst, label='Worst Case')

# Plot average-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_average, label='Average Case')

plt.xlabel('Text Length')
plt.ylabel('Runtime (seconds)')
plt.title('Naive String Matching Algorithm Runtimes')
plt.legend()
plt.grid(True)
plt.show()
ss