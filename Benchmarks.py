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

# Benchmarking for all algorithms
def benchmarks(input_sizes):
    algorithms = {
        "Naive String Matching": (naive_string_match, benchmark_naive_string_match),
        "Rabin-Karp": (rabin_karp, benchmark_rabin_karp),
        "Finite Automaton Match": (finite_automaton_match, benchmark_finite_automaton_match),
        "Knuth-Morris-Pratt": (knuth_morris_pratt, benchmark_knuth_morris_pratt)
    }

    for algorithm_name, (algorithm_func, benchmark_func) in algorithms.items():
        for pattern_length, text_length in input_sizes:
            best_case_pattern, best_case_text, worst_case_pattern, worst_case_text, average_case_pattern, average_case_text = generate_test_cases(pattern_length, text_length)
            
            if algorithm_name == "Finite Automaton Match":
                runtime_best = benchmark_func(best_case_pattern, best_case_text, set(average_case_text))
                runtime_worst = benchmark_func(worst_case_pattern, worst_case_text, set(average_case_text))
                runtime_average = benchmark_func(average_case_pattern, average_case_text, set(average_case_text))
            else:
                runtime_best = benchmark_func(best_case_pattern, best_case_text)
                runtime_worst = benchmark_func(worst_case_pattern, worst_case_text)
                runtime_average = benchmark_func(average_case_pattern, average_case_text)
            
            print(f"{algorithm_name} for input size {text_length}: Best Case: {runtime_best} seconds, Worst Case: {runtime_worst} seconds, Average Case: {runtime_average} s")

# Perform benchmarks
benchmarks(input_sizes)
