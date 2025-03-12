# Extreme hard level

Here are 25 extremely hard Python quizzes using the `assert` keyword. These tasks push the boundaries  
of algorithmic complexity, advanced data structures, mathematical reasoning, and optimization techniques. 
They are designed to be exceptionally challenging, often requiring deep knowledge of computer science  
concepts and creative problem-solving.

---

## Task 1

```python
n = 5

non_decreasing_sequences = ...  # Count non-decreasing sequences of length n using digits 0-9

assert non_decreasing_sequences == 252  # Using stars and bars: C(9+5, 5) = C(14, 5)
print('passed')
```

## Task 2

```python
text = "ababc"

lps = ...  # Longest proper prefix which is also suffix array (KMP algorithm)

assert lps == [0, 0, 1, 2, 0]
print('passed')
```

## Task 3

```python
grid = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]

shortest_path_all_ones = ...  # Shortest path from top-left to bottom-right visiting all 1s (TSP-like)

assert shortest_path_all_ones == 6  # Path visiting all 5 ones
print('passed')
```

## Task 4

```python
numbers = [1, 2, 3, 4, 5]

partition_diff = ...  # Minimum difference between two partitions of equal sum (or closest possible)

assert partition_diff == 1  # [1, 4] (5) vs [2, 3, 5] (10)
print('passed')
```

## Task 5
```python
n = 20

nth_catalan = ...  # nth Catalan number using recursive formula

assert nth_catalan == 1767263190
print('passed')
```

## Task 6

```python
graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}

min_cut = ...  # Minimum cut in undirected graph (Stoer-Wagner algorithm simplified)

assert min_cut == 2
print('passed')
```

## Task 7

```python
numbers = [1, 2, 3, 4, 5, 6]

max_non_adjacent_sum = ...  # Maximum sum of non-adjacent elements

assert max_non_adjacent_sum == 12  # [1, 3, 5] or [2, 4, 6]
print('passed')
```

## Task 8
```python
text = "abcbadef"

longest_palindromic_substring = ...  # Longest palindromic substring (Manacher's algorithm simplified)

assert longest_palindromic_substring == "bcb"
print('passed')
```

## Task 9

```python
n = 5
k = 3

combinations_mod = ...  # Number of ways to choose k items from n with modular arithmetic (mod 10^9 + 7)

assert combinations_mod == 10
print('passed')
```

## Task 10

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

unique_paths_with_obstacles = ...  # Unique paths with diagonal moves, 5 is obstacle

assert unique_paths_with_obstacles == 26
print('passed')
```

## Task 11

```python
numbers = [2, 3, 5, 7, 11]

subset_gcd = ...  # Maximum GCD of any subset

assert subset_gcd == 1  # All primes, GCD of any subset > 1 is product of primes or 1
print('passed')
```

## Task 12

```python
tree = {'val': 1, 'left': {'val': 2, 'left': {'val': 4, 'left': None, 'right': None}, 'right': None}, 'right': {'val': 3, 'left': None, 'right': None}}

max_path_sum = ...  # Maximum path sum in binary tree (any node to any node)

assert max_path_sum == 10  # Path: 4->2->1->3
print('passed')
```

## Task 13

```python
n = 100

prime_factors_count = ...  # Count distinct prime factors up to n

assert prime_factors_count == 25  # Primes: 2, 3, 5, ..., 97
print('passed')
```

## Task 14

```python
numbers = [1, 2, 2, 3, 3, 4]

k = 2
k_frequent_elements = ...  # Top k frequent elements

assert sorted(k_frequent_elements) == [2, 3]
print('passed')
```

## Task 15

```python
grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

max_island_area = ...  # Maximum area of an island (connected 1s)

assert max_island_area == 4
print('passed')
```

## Task 16

```python
n = 5

gray_code = ...  # Generate n-bit Gray code sequence

assert gray_code == [0, 1, 3, 2, 6, 7, 5, 4]
print('passed')
```

## Task 17

```python
numbers = [1, 2, 3, 4, 5]

max_product_subarray = ...  # Maximum product subarray

assert max_product_subarray == 120  # [1, 2, 3, 4, 5]
print('passed')
```

## Task 18

```python
text = "aabab"

regex_match = ...  # Check if text matches pattern "a*b*" using dynamic programming

assert regex_match == True
print('passed')
```

## Task 19

```python
n = 4

magic_square = ...  # Generate a 4x4 magic square (all rows, cols, diagonals sum to same value)

assert sum(magic_square[0]) == 34 and all(sum(row) == 34 for row in magic_square) and all(sum(col) for col in zip(*magic_square)) == [34]*4
print('passed')
```

## Task 20

```python
numbers = [1, 3, 5, 6, 7]

min_jumps = ...  # Minimum jumps to reach end, where jump[i] = max steps from i

assert min_jumps == 2  # Jump from 1 to 5, then 5 to 7
print('passed')
```

## Task 21

```python
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}

articulation_points = ...  # Find articulation points in undirected graph

assert sorted(articulation_points) == [0]
print('passed')
```

## Task 22

```python
n = 10

partition_count = ...  # Number of integer partitions of n

assert partition_count == 42
print('passed')
```

## Task 23

```python
numbers = [4, 2, 7, 1, 3]

longest_arithmetic_subsequence = ...  # Length of longest arithmetic subsequence

assert longest_arithmetic_subsequence == 3  # [4, 2, 1] or [7, 1, 3]
print('passed')
```

## Task 24

```python
text = "abcde"

min_cut_palindrome = ...  # Minimum cuts to partition into palindromes

assert min_cut_palindrome == 4  # Each character is a palindrome
print('passed')
```

## Task 25

```python
n = 5

hamiltonian_paths = ...  # Number of Hamiltonian paths in a complete graph K_n

assert hamiltonian_paths == 120  # n!/2 for n=5
print('passed')
```



