import time
import string
from collections import Counter
import random

def normalize_string(s):
    """
    Helper function to remove spaces and convert to lowercase.
    Complexity: O(N)
    """
    return s.replace(" ", "").lower()

# --- APPROACH 1: Sorting
def are_anagrams_sorting(s1, s2):
    """
    Determines if s1 and s2 are anagrams by sorting.
    Space Complexity: O(N) to store the sorted list.
    """
    s1_clean = normalize_string(s1)
    s2_clean = normalize_string(s2)
    
    if len(s1_clean) != len(s2_clean):
        return False
        
    return sorted(s1_clean) == sorted(s2_clean)

# --- APPROACH 2: Hash Map
def are_anagrams_hashing(s1, s2):
    """
    Determines if s1 and s2 are anagrams using a dictionary (Hash Map).
    Time Complexity: O(N)
    Space Complexity: O(K) where K is the unique character set (approx constant for ASCII).
    """
    s1_clean = normalize_string(s1)
    s2_clean = normalize_string(s2)

    if len(s1_clean) != len(s2_clean):
        return False

    counts = {}

    for char in s1_clean:
        counts[char] = counts.get(char, 0) + 1

    for char in s2_clean:
        if char not in counts:
            return False
        counts[char] -= 1

        if counts[char] == 0:
            del counts[char]

    return len(counts) == 0

# --- APPROACH 3: collections.Counter
def are_anagrams_counter(s1, s2):
    """
    The 'Real World' Python approach using collections.Counter.
    Under the hood, this is also O(N).
    """
    return Counter(normalize_string(s1)) == Counter(normalize_string(s2))


def run_benchmark():
    print("--- Generating large strings for benchmark ---")
    N = 10**7
    chars = string.ascii_lowercase
    base_str = ''.join(random.choices(chars, k=N))

    anagram_list = list(base_str)
    random.shuffle(anagram_list)
    compare_str = ''.join(anagram_list)

    print(f"String Length: {N:,} characters")
    print("-" * 50)

    # Measure Sorting
    start = time.perf_counter()
    res_sort = are_anagrams_sorting(base_str, compare_str)
    end = time.perf_counter()
    print(f"Sorting Approach: {end - start:.4f} seconds")

    # Measure Hashing
    start = time.perf_counter()
    res_hash = are_anagrams_hashing(base_str, compare_str)
    end = time.perf_counter()
    print(f"Hashing Approach:       {end - start:.4f} seconds")

    # Measure Counter
    start = time.perf_counter()
    res_count = are_anagrams_counter(base_str, compare_str)
    end = time.perf_counter()
    print(f"Counter Approach:       {end - start:.4f} seconds")

if __name__ == "__main__":

    run_benchmark()