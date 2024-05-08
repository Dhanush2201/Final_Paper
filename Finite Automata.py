# String Matching with Finite Automata
def compute_transition_function(pattern, alphabet):
    m = len(pattern)
    transition = [{char: 0 for char in alphabet} for _ in range(m + 1)]
    for q in range(m + 1):
        for char in alphabet:
            k = min(m, q + 1)
            while not (pattern[:q] + char).endswith(pattern[:k]):
                k -= 1
            transition[q][char] = k
    return transition

def finite_automaton_match(pattern, text, alphabet):
    occurrences = []
    n = len(text)
    m = len(pattern)
    transition = compute_transition_function(pattern, alphabet)
    q = 0
    for i in range(n):
        q = transition[q][text[i]]
        if q == m:
            occurrences.append(i - m + 1)
    return occurrences

def benchmark_finite_automaton_match(pattern, text, alphabet):
    return timeit.timeit(lambda: finite_automaton_match(pattern, text, alphabet), number=10)

def finite_automaton_benchmarks(input_sizes):
    all_runtimes_best = []
    all_runtimes_worst = []
    all_runtimes_average = []

    for pattern_length, text_length in input_sizes:
        best_case_pattern, best_case_text, worst_case_pattern, worst_case_text, average_case_pattern, average_case_text = generate_test_cases(pattern_length, text_length)
        
        runtime_best = benchmark_finite_automaton_match(best_case_pattern, best_case_text, set(average_case_text))
        runtime_worst = benchmark_finite_automaton_match(worst_case_pattern, worst_case_text, set(average_case_text))
        runtime_average = benchmark_finite_automaton_match(average_case_pattern, average_case_text, set(average_case_text))
        
        all_runtimes_best.append(runtime_best)
        all_runtimes_worst.append(runtime_worst)
        all_runtimes_average.append(runtime_average)

    return all_runtimes_best, all_runtimes_worst, all_runtimes_average

# Input sizes to test
input_sizes = [(5, 100), (10, 200), (20, 400), (50, 1000), (100, 2000)]

# Benchmarking for Finite Automata Matching
algorithm_runtimes_best, algorithm_runtimes_worst, algorithm_runtimes_average = finite_automaton_benchmarks(input_sizes)

plt.figure(figsize=(10, 6))

# Plot best-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_best, label='Best Case')

# Plot worst-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_worst, label='Worst Case')

# Plot average-case runtimes
plt.plot([size[1] for size in input_sizes], algorithm_runtimes_average, label='Average Case')

plt.xlabel('Text Length')
plt.ylabel('Runtime (seconds)')
plt.title('Finite Automata Matching Algorithm Runtimes')
plt.legend()
plt.grid(True)
plt.show()
