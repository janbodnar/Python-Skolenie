# Hard level tasks

Here are 20 hard-level Python quizzes using the `assert` keyword. These tasks involve advanced  
concepts like recursion, complex data structures, algorithmic challenges, and multi-step processing,  
making them significantly more challenging than the medium-level tasks.

---

## Task 1
```python
numbers = [1, 2, 3, 4, 5]

subsets = ...  # Generate all possible subsets (power set)

assert len(subsets) == 32 and sorted(subsets) == [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 5], [1, 2, 4], [1, 2, 4, 5], [1, 2, 5], [1, 3], [1, 3, 4], [1, 3, 4, 5], [1, 3, 5], [1, 4], [1, 4, 5], [1, 5], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 5], [2, 4], [2, 4, 5], [2, 5], [3], [3, 4], [3, 4, 5], [3, 5], [4], [4, 5], [5]]
print('passed')
```

## Task 2
```python
text = "aabbbcccc"

run_length_encoded = ...  # Run-length encoding: (count, char) pairs

assert run_length_encoded == [(2, 'a'), (3, 'b'), (4, 'c')]
print('passed')
```

## Task 3
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

spiral_order = ...  # Traverse matrix in spiral order

assert spiral_order == [1, 2, 3, 6, 9, 8, 7, 4, 5]
print('passed')
```

## Task 4
```python
numbers = [4, 2, 7, 1, 8, 3, 6]

max_subarray_sum = ...  # Maximum subarray sum (Kadane's algorithm)

assert max_subarray_sum == 21  # [2, 7, 1, 8, 3]
print('passed')
```

## Task 5
```python
n = 5

fibonacci = ...  # Generate Fibonacci sequence up to n terms recursively

assert fibonacci == [0, 1, 1, 2, 3]
print('passed')
```

## Task 6
```python
data = {'a': {'b': 1, 'c': 2}, 'd': {'e': {'f': 3}}}

flattened = ...  # Flatten nested dictionary with dot notation

assert flattened == {'a.b': 1, 'a.c': 2, 'd.e.f': 3}
print('passed')
```

## Task 7
```python
numbers = [1, 1, 2, 3, 3, 4, 4, 4]

majority_element = ...  # Find element appearing more than n/2 times (Boyer-Moore voting)

assert majority_element == 4
print('passed')
```

## Task 8
```python
text = "((a+b)*(c-d))"

is_balanced = ...  # Check if parentheses are balanced

assert is_balanced == True
print('passed')
```

## Task 9
```python
numbers = [1, 5, 2, 9, 3, 7]

longest_increasing_subsequence = ...  # Length of longest increasing subsequence

assert longest_increasing_subsequence == 4  # [1, 2, 3, 7]
print('passed')
```

## Task 10
```python
graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}

connected_components = ...  # Number of connected components in undirected graph

assert connected_components == 1
print('passed')
```

## Task 11
```python
n = 4

permutations = ...  # Generate all permutations of [1, 2, 3, 4]

assert len(permutations) == 24 and [1, 2, 3, 4] in permutations and [4, 3, 2, 1] in permutations
print('passed')
```

## Task 12
```python
intervals = [(1, 4), (2, 5), (7, 9), (3, 6)]

merged = ...  # Merge overlapping intervals

assert merged == [(1, 6), (7, 9)]
print('passed')
```

## Task 13
```python
numbers = [3, 30, 34, 5, 9]

largest_number = ...  # Form largest possible number by arranging digits

assert largest_number == "9534330"
print('passed')
```

## Task 14
```python
tree = {'val': 1, 'left': {'val': 2, 'left': None, 'right': None}, 'right': {'val': 3, 'left': None, 'right': None}}

preorder = ...  # Preorder traversal of binary tree

assert preorder == [1, 2, 3]
print('passed')
```

## Task 15
```python
matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

shortest_path = ...  # Shortest path from top-left to bottom-right (only right/down, 0 is obstacle)

assert shortest_path == 6  # Path: 1->2->3->6->9
print('passed')
```

## Task 16
```python
numbers = [2, 3, 6, 7]

target_combinations = ...  # Combinations that sum to 7

assert sorted(target_combinations) == [[2, 3, 2], [7]]
print('passed')
```

## Task 17
```python
text = "abacabad"

suffix_array = ...  # Construct suffix array (indices of sorted suffixes)

assert suffix_array == [7, 5, 0, 2, 3, 1, 6, 4]
print('passed')
```

## Task 18
```python
data = [1, 2, [3, 4], [5, [6, 7]]]

deep_flattened = ...  # Deep flatten nested list

assert deep_flattened == [1, 2, 3, 4, 5, 6, 7]
print('passed')
```

## Task 19
```python
numbers = [1, 2, 3, 4]

k = 2
kth_permutation = ...  # Find kth lexicographical permutation (1-based index)

assert kth_permutation == [1, 3, 2, 4]
print('passed')
```

## Task 20
```python
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

min_path_sum = ...  # Minimum path sum from top-left to bottom-right (only right/down)

assert min_path_sum == 7  # Path: 1->3->1->2->1
print('passed')
```


