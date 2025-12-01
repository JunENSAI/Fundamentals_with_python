## Anagram efficiency

Implement a function **are_anagrams(s1: str, s2: str) -> bool** that determines if two strings contain the exact same character counts.

- Naive Approach: Sort both strings and compare them: return sorted(s1) == sorted(s2). Python's Timsort is O(n log n).

- Optimized Approach: Use a frequency counter (Hash Map). Iterate through s1 to count characters (+1), then iterate through s2 to decrement (-1). If the dictionary values are all zero, they are anagrams.

- Complexity Constraint: The solution must operate in O(n) time complexity.

- Edge Cases: The solution must handle case sensitivity and ignore whitespace if required by the spec. This reinforces the utility of the Space-Time tradeoff, using O(k) space (where k is the character set) to achieve O(n) time.