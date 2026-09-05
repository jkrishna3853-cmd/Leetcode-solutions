# 🧩 LeetCode Practice & Pattern Playbook

![LeetCode Sync](https://img.shields.io/badge/LeetCode-Auto--Sync-orange?style=flat-square&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20C%2B%2B%20%7C%20Java-blue?style=flat-square)
![Progress](https://img.shields.io/badge/Problems%20Solved-000%2F150-brightgreen?style=flat-square)

> A structured collection of LeetCode solutions organized by core algorithmic patterns, categorized for targeted technical interview preparation. Automatic sync powered by **LeetHub v2**.

---

## 📊 Progress Dashboard

| Difficulty | Solved | Target | Status |
| :--- | :---: | :---: | :---: |
| 🟩 **Easy** | 8 | 40 | `░░░░░░░░░░` 20% |
| 🟨 **Medium** | 12 | 90 | `░░░░░░░░░░` 12% |
| 🟥 **Hard** | 3 | 20 | `░░░░░░░░░░` 10% |
| **Total** | **21** | **150** | **14% Complete** |

---

## 🎯 Solutions by Algorithmic Pattern

### 1. Arrays & Hashing

| # | Problem | Difficulty | Solution | Time | Space | Core Concept |
| :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟩 Easy | [Python](./01-arrays-and-hashing/0001-two-sum/solution.py) | $O(N)$ | $O(N)$ | Hash Map lookup |
| 0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟩 Easy | [Python](./01-arrays-and-hashing/0217-contains-duplicate/solution.py) | $O(N)$ | $O(N)$ | Hash Set insertion |
| 0049 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟨 Medium | [Python](./01-arrays-and-hashing/0049-group-anagrams/solution.py) | $O(N \cdot K)$ | $O(N \cdot K)$ | Frequency map key |

### 2. Two Pointers

| # | Problem | Difficulty | Solution | Time | Space | Core Concept |
| :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| 0125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟩 Easy | [Python](./02-two-pointers/0125-valid-palindrome/solution.py) | $O(N)$ | $O(1)$ | Opposite ends convergence |
| 0015 | [3Sum](https://leetcode.com/problems/3sum/) | 🟨 Medium | [Python](./02-two-pointers/0015-3sum/solution.py) | $O(N^2)$ | $O(1)$ | Sort + 2-pointer sweep |

### 3. Sliding Window

| # | Problem | Difficulty | Solution | Time | Space | Core Concept |
| :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| 0121 | [Best Time to Buy & Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟩 Easy | [Python](./03-sliding-window/0121-best-time-to-buy-and-sell-stock/solution.py) | $O(N)$ | $O(1)$ | Track min price & max profit |
| 0003 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟨 Medium | [Python](./03-sliding-window/0003-longest-substring-without-repeating-characters/solution.py) | $O(N)$ | $O(N)$ | Dynamic window + Set |

### 4. Trees & Graphs

| # | Problem | Difficulty | Solution | Time | Space | Core Concept |
| :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| 0226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟩 Easy | [Python](./04-trees-and-graphs/0226-invert-binary-tree/solution.py) | $O(N)$ | $O(H)$ | Recursive DFS |
| 0200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟨 Medium | [Python](./04-trees-and-graphs/0200-number-of-islands/solution.py) | $O(M \cdot N)$ | $O(M \cdot N)$ | Grid BFS / DFS traversal |

---

## 🛠️ Repository Organization

```text
.
├── 01-arrays-and-hashing/
│   └── 0001-two-sum/
│       ├── README.md        <-- Generated description & performance details
│       └── solution.py      <-- Clean solution
├── 02-two-pointers/
├── 03-sliding-window/
└── README.md                <-- Master index (This file)

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0018-4sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0018-4sum) |
| [0027-remove-element](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0027-remove-element) |
| [0031-next-permutation](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0031-next-permutation) |
| [0033-search-in-rotated-sorted-array](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0033-search-in-rotated-sorted-array) |
| [0034-find-first-and-last-position-of-element-in-sorted-array](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0034-find-first-and-last-position-of-element-in-sorted-array) |
| [0035-search-insert-position](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0035-search-insert-position) |
| [0036-valid-sudoku](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0036-valid-sudoku) |
| [0039-combination-sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0040-combination-sum-ii) |
| [0041-first-missing-positive](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0041-first-missing-positive) |
| [0042-trapping-rain-water](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0045-jump-game-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0045-jump-game-ii) |
| [0046-permutations](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0046-permutations) |
| [0047-permutations-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0047-permutations-ii) |
| [0048-rotate-image](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0048-rotate-image) |
| [0049-group-anagrams](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0049-group-anagrams) |
| [0051-n-queens](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0051-n-queens) |
| [0053-maximum-subarray](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0053-maximum-subarray) |
## Two Pointers
|  |
| ------- |
| [0018-4sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0018-4sum) |
| [0019-remove-nth-node-from-end-of-list](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0027-remove-element](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0027-remove-element) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0031-next-permutation](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0031-next-permutation) |
| [0042-trapping-rain-water](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0042-trapping-rain-water) |
## Sorting
|  |
| ------- |
| [0018-4sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0018-4sum) |
| [0047-permutations-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0047-permutations-ii) |
| [0049-group-anagrams](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0049-group-anagrams) |
## Hash Table
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0030-substring-with-concatenation-of-all-words](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0030-substring-with-concatenation-of-all-words) |
| [0036-valid-sudoku](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0036-valid-sudoku) |
| [0041-first-missing-positive](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0041-first-missing-positive) |
| [0049-group-anagrams](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0049-group-anagrams) |
## String
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0020-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0020-valid-parentheses) |
| [0022-generate-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0022-generate-parentheses) |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
| [0030-substring-with-concatenation-of-all-words](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0030-substring-with-concatenation-of-all-words) |
| [0032-longest-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0032-longest-valid-parentheses) |
| [0038-count-and-say](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0038-count-and-say) |
| [0043-multiply-strings](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0043-multiply-strings) |
| [0044-wildcard-matching](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0044-wildcard-matching) |
| [0049-group-anagrams](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0049-group-anagrams) |
## Backtracking
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0022-generate-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0022-generate-parentheses) |
| [0039-combination-sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0040-combination-sum-ii) |
| [0046-permutations](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0046-permutations) |
| [0047-permutations-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0047-permutations-ii) |
| [0051-n-queens](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0051-n-queens) |
| [0052-n-queens-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0052-n-queens-ii) |
## Linked List
|  |
| ------- |
| [0019-remove-nth-node-from-end-of-list](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0021-merge-two-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0021-merge-two-sorted-lists) |
| [0023-merge-k-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0023-merge-k-sorted-lists) |
| [0025-reverse-nodes-in-k-group](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0025-reverse-nodes-in-k-group) |
## Stack
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0020-valid-parentheses) |
| [0032-longest-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0032-longest-valid-parentheses) |
| [0042-trapping-rain-water](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0042-trapping-rain-water) |
## Bracket Sequences
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0020-valid-parentheses) |
| [0022-generate-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0022-generate-parentheses) |
| [0032-longest-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0032-longest-valid-parentheses) |
## Recursion
|  |
| ------- |
| [0021-merge-two-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0021-merge-two-sorted-lists) |
| [0025-reverse-nodes-in-k-group](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0025-reverse-nodes-in-k-group) |
| [0044-wildcard-matching](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0044-wildcard-matching) |
| [0050-powx-n](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0050-powx-n) |
## Dynamic Programming
|  |
| ------- |
| [0022-generate-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0022-generate-parentheses) |
| [0032-longest-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0032-longest-valid-parentheses) |
| [0042-trapping-rain-water](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0044-wildcard-matching](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0044-wildcard-matching) |
| [0045-jump-game-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0045-jump-game-ii) |
| [0053-maximum-subarray](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0053-maximum-subarray) |
## Divide and Conquer
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0023-merge-k-sorted-lists) |
| [0053-maximum-subarray](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0053-maximum-subarray) |
## Heap (Priority Queue)
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0023-merge-k-sorted-lists) |
## Merge Sort
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0023-merge-k-sorted-lists) |
## Tournament Sort
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0023-merge-k-sorted-lists) |
## String Matching
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Z Algorithm
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Knuth–Morris–Pratt Algorithm
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Boyer–Moore String-Search Algorithm
|  |
| ------- |
| [0028-find-the-index-of-the-first-occurrence-in-a-string](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0028-find-the-index-of-the-first-occurrence-in-a-string) |
## Math
|  |
| ------- |
| [0029-divide-two-integers](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0029-divide-two-integers) |
| [0043-multiply-strings](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0043-multiply-strings) |
| [0048-rotate-image](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0048-rotate-image) |
| [0050-powx-n](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0050-powx-n) |
## Bit Manipulation
|  |
| ------- |
| [0029-divide-two-integers](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0029-divide-two-integers) |
## Sliding Window
|  |
| ------- |
| [0030-substring-with-concatenation-of-all-words](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0030-substring-with-concatenation-of-all-words) |
## Binary Search
|  |
| ------- |
| [0033-search-in-rotated-sorted-array](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0033-search-in-rotated-sorted-array) |
| [0034-find-first-and-last-position-of-element-in-sorted-array](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0034-find-first-and-last-position-of-element-in-sorted-array) |
| [0035-search-insert-position](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0035-search-insert-position) |
## Matrix
|  |
| ------- |
| [0036-valid-sudoku](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0036-valid-sudoku) |
| [0048-rotate-image](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0048-rotate-image) |
## Monotonic Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0042-trapping-rain-water) |
## Simulation
|  |
| ------- |
| [0043-multiply-strings](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0043-multiply-strings) |
## Greedy
|  |
| ------- |
| [0044-wildcard-matching](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0044-wildcard-matching) |
| [0045-jump-game-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0045-jump-game-ii) |
## Algorithm X
|  |
| ------- |
| [0051-n-queens](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0051-n-queens) |
| [0052-n-queens-ii](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0052-n-queens-ii) |
<!---LeetCode Topics End-->
