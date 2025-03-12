# Python Tasks

This section contains tasks to deepen your knowledge of the Python programming language.

In some examples, the following file is used:

File `battle.txt`:

```
The Battle of Gettysburg was fought between the Union and the Confederate States
during the American Civil War, from July 1 to July 3, 1863.
```

Try to solve the following tasks:

---

### Basic Tasks

1. Display the Python version you are using.
2. Display the operating system version.
3. Display today's date.
4. Display the current local time.
5. Display the current universal time (UTC).
6. Display the current time in New York, Tokyo, and London.
7. Write a program to launch the Calculator application (or another app).
8. Create a program to print the lyrics of "Twinkle, Twinkle, Little Star" with a loop for repetition.
9. Print all multiples of 7 between 0 and 100 (inclusive).
10. Generate and print 15 random integers between 10 and 50 (inclusive).
11. Print the elements of the list `[1, 3, 5, 7, 9]` as a comma-separated string (e.g., `1, 3, 5, 7, 9`).
12. Calculate the average of numbers in the list `[10, 20, 30, 40, 50]`.
13. Sort the list `[6, 2, 8, 4, 10, 1, 9]` in ascending order without using `sort()`.
14. Calculate the sum of squares of numbers in the tuple `(1, 2, 3, 4)`.
15. From the list `[1, 2, 3, 4]`, create a new list where each element is doubled.
16. Print all numbers from 1 to 50 that are not divisible by 3.
17. Calculate the sum of factorials from 1 to 5 (i.e., 1! + 2! + 3! + 4! + 5!).
18. Generate 30 random numbers between 0 and 20 and find the most frequent number.
19. Write a function to capitalize the first letter of a string (e.g., `python` → `Python`).
20. Write a function to convert a number to its negative (e.g., `5` → `-5`).

---

### Easy to Intermediate Tasks

21. Write a function to join the tuple `('apple', 'banana', 'orange')` into a single string with spaces.
22. Write a function `has_common_letters` to check if two words share any letters (e.g., `cat` and `dog`).
23. Write a function `is_symmetric` to check if a string reads the same forwards and backwards ignoring case (e.g., `Racecar`).
24. Count the number of consonants in the sentence "Rain falls gently".
25. Given the list `[2, 4, 6, 8, 10, 12]`, calculate the product, average, and median.
26. Given the list `['red', 'blue', 'red', 'green', 'blue', 'yellow']`, create a list of unique colors.
27. Compute the value of `2^10` and round it to the nearest integer.
28. Convert numbers from the tuple `(10, 50, 100, 500)` to their hexadecimal representation.
29. Read the file `battle.txt` and print its contents.
30. Append the text "This is a historic event." to the file `battle.txt`.
31. Count the number of lines in the file `battle.txt`.
32. Print the current working directory of your Python script.
33. Create a new directory named `test_folder` in your current working directory.
34. Ask the user for the length of a rectangle’s sides and calculate its perimeter and area.
35. Calculate the number of days until the next summer solstice (assume June 21).
36. Calculate the number of weeks since the Declaration of Independence (July 4, 1776).
37. Convert a list of tuples `[(1, 2), (3, 4), (5, 6)]` into a single list `[1, 2, 3, 4, 5, 6]`.
38. A movie ticket costs $9.50, and 1200 tickets are sold. Calculate the total revenue with tax (8%).
39. Install the `requests` module using pip and use it to fetch the status code of `https://python.org`.
40. Fetch and print the text content of all paragraph tags (`<p>`) from `https://example.com`.

---

### Intermediate Tasks

41. Print the ASCII values of all characters in the string "Hello" in a 5-column format.
42. Read the file `battle.txt` and count the number of characters (excluding spaces and newlines).
43. Read the file `battle.txt` and find the longest word.
44. Generate 50 random numbers between -10 and 10 and write them to `numbers.txt`, one per line.
45. Read `numbers.txt` and calculate the sum of positive numbers and the count of negative numbers.
46. Encrypt the message "Secret plan revealed" using a Vigenère cipher with key "KEY", then decrypt it.
47. Create a Flask web app with two routes: "/" displays "Home" and "/about" displays "About Us".
48. Create a line chart using Matplotlib for temperature data: `(32, 35, 28, 30, 33)` over days `(Mon, Tue, Wed, Thu, Fri)`.
49. Using NumPy, calculate the inverse of a 3x3 matrix of your choice (ensure it’s invertible).
50. Create a Tkinter GUI with a text entry field and a button that displays the entered text in a label.
51. Write a function to find the third largest number in the list `[7, 3, 9, 1, 6, 2, 8]`.
52. Generate all possible sums of pairs from the list `[2, 4, 6, 8]` (e.g., `6, 8, 10, 12, 14`).
53. Convert a binary string (e.g., `1010`) to its decimal equivalent without built-in functions.
54. Write a function to find all factors of a number (e.g., `24` → `[1, 2, 3, 4, 6, 8, 12, 24]`).
55. Calculate the sum of squares of all even numbers from 1 to 200.

---

### Intermediate to Advanced Tasks

56. Write an iterative function to compute the nth Tribonacci number (e.g., n=7, where T(n) = T(n-1) + T(n-2) + T(n-3)).
57. Implement a function to remove duplicates from an unsorted list (e.g., `[3, 1, 3, 5, 1, 7]` → `[3, 1, 5, 7]`).
58. Find all pairs in the list `[2, 4, 3, 5, 7, 8]` that sum to 10.
59. Write a function to reverse a list in chunks of size k (e.g., `[1, 2, 3, 4, 5, 6]`, k=2 → `[2, 1, 4, 3, 6, 5]`).
60. Parse a simple CSV string (e.g., `"name,age\nAlice,25\nBob,30"`) and print it as a list of dictionaries.
61. Implement a circular buffer class with add and remove methods, and test it with 5 elements.
62. Write a function to find the shortest word in a list of strings (e.g., `["cat", "elephant", "dog"]` → `"cat"`).
63. Create a dictionary mapping numbers to their English names for `[1, 2, 3]` (e.g., `{1: "one", 2: "two", 3: "three"}`).
64. Simulate flipping a coin 500 times and calculate the percentage of heads.
65. Implement selection sort to sort the list `[29, 10, 14, 37, 13]`.

---

### Advanced Tasks

66. Write a function to count the number of nested levels in a dictionary (e.g., `{"a": {"b": 1, "c": {"d": 2}}}` → 3).
67. Implement an interpolation search algorithm to find an element in a sorted list (e.g., `6` in `[1, 2, 3, 4, 6, 8, 10]`).
68. Write a function to solve the 8-puzzle problem using a simple heuristic (provide a 3x3 grid).
69. Create a generator function to yield perfect squares up to 1000.
70. Implement a priority queue class with enqueue and dequeue methods, and test it with numbers.
71. Write a function to find the longest common subsequence of two strings (e.g., `ABCDGH` and `AEDFHR` → `ADH`).
72. Generate all combinations of size 2 from the list `[1, 2, 3, 4]`.
73. Write a function to validate a simple arithmetic expression (e.g., `"3 + (5 * 2)"` is valid, `"3 + )"` is not).
74. Find the number of unique paths in a 4x4 grid with obstacles at `(1, 1)` and `(2, 2)` using only right/down moves.
75. Implement a binary search tree (BST) and insert values `[5, 3, 7, 1, 4]`, then print the inorder traversal.

---

### Very Advanced Tasks

76. Write a function to verify if a 9x9 Sudoku grid is valid (doesn’t need to solve, just check rules).
77. Implement the 0/1 Knapsack problem for items with weights `[2, 3, 4]` and values `[10, 15, 20]`, capacity 6.
78. Find the length of the longest alternating subsequence in `[1, 5, 4, 3, 6, 2]` (e.g., up-down-up).
79. Write a function to transpose a 4x4 matrix without NumPy.
80. Implement Bellman-Ford algorithm for shortest paths in a graph with negative weights (e.g., `{0: {1: 4, 2: 8}, 1: {2: -2}, 2: {}}`).
81. Compute the nth Bell number iteratively (e.g., n=4, partitions of a set).
82. Generate a 3x3 magic square with numbers 1-9 where all sums are 15.
83. Implement a simple Monte Carlo simulation to estimate π by throwing darts at a square with an inscribed circle.
84. Write a function to compute the bipartite matching in a graph (e.g., `{0: [3, 4], 1: [3], 2: [4]}`).
85. Compute the area of a polygon given vertices `[(0, 0), (2, 0), (2, 2), (0, 2)]` using the shoelace formula.

---

### Extremely Hard Tasks

86. Implement the Lempel-Ziv-Welch (LZW) compression algorithm for the string `TOBEORNOTTOBE`.
87. Write a function to place 5 queens on a 5x5 chessboard so no two attack each other.
88. Find the length of the shortest uncommon subsequence between `ABCDE` and `ACE` (not present in both).
89. Implement a suffix tree for the string `BANANA` and list all suffixes.
90. Write a function to decode a Huffman-encoded string given a code table (e.g., `{'A': '0', 'B': '10', 'C': '11'}`).
91. Implement Prim’s algorithm for a minimum spanning tree (e.g., edges `[(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 5)]`).
92. Simulate a simple Markov chain with states `["sunny", "rainy"]` and a transition matrix for 10 steps.
93. Write a function to find all biconnected components in a graph (e.g., `{0: [1, 2], 1: [0, 2], 2: [0, 1]}`).
94. Solve the Job Scheduling problem for jobs with deadlines and profits (e.g., `[(1, 4), (2, 5), (3, 6)]`).
95. Implement a Fenwick tree (binary indexed tree) for range sum queries on `[2, 4, 6, 8]`.

---

### Expert-Level Tasks

96. Write a function to perform discrete cosine transform (DCT) on a list of 8 numbers.
97. Implement an AVL tree and insert values `[10, 20, 30, 40, 50]`, ensuring balance after each insertion.
98. Simulate a distributed consensus algorithm (e.g., simplified Raft) with 3 nodes agreeing on a value.
99. Write a function to compute the Smith-Waterman local alignment score for two DNA sequences (e.g., `AGCT` and `ACGT`).
100. Implement a parser for a context-free grammar (e.g., `S -> aS | bS | ε`) and test string `aab`.

