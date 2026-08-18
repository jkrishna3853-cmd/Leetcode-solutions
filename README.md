# 🧩 LeetCode Practice & Pattern Playbook

![LeetCode Sync](https://img.shields.io/badge/LeetCode-Auto--Sync-orange?style=flat-square&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20C%2B%2B%20%7C%20Java-blue?style=flat-square)
![Progress](https://img.shields.io/badge/Problems%20Solved-000%2F150-brightgreen?style=flat-square)

> A structured collection of LeetCode solutions organized by core algorithmic patterns, categorized for targeted technical interview preparation. Automatic sync powered by **LeetHub v2**.

---

## 📊 Progress Dashboard

| Difficulty | Solved | Target | Status |
| :--- | :---: | :---: | :---: |
| 🟩 **Easy** | 5 | 40 | `░░░░░░░░░░` 10% |
| 🟨 **Medium** | 6 | 90 | `░░░░░░░░░░` 6% |
| 🟥 **Hard** | 0 | 20 | `░░░░░░░░░░` 0% |
| **Total** | **9** | **150** | **6% Complete** |

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
## Two Pointers
|  |
| ------- |
| [0018-4sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0018-4sum) |
| [0019-remove-nth-node-from-end-of-list](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0027-remove-element](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0027-remove-element) |
| [0031-next-permutation](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0031-next-permutation) |
## Sorting
|  |
| ------- |
| [0018-4sum](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0018-4sum) |
## Hash Table
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0017-letter-combinations-of-a-phone-number) |
## String
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0020-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0020-valid-parentheses) |
## Backtracking
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0017-letter-combinations-of-a-phone-number) |
## Linked List
|  |
| ------- |
| [0019-remove-nth-node-from-end-of-list](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0019-remove-nth-node-from-end-of-list) |
## Stack
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0020-valid-parentheses) |
## Bracket Sequences
|  |
| ------- |
| [0020-valid-parentheses](https://github.com/jkrishna3853-cmd/Leetcode-solutions/tree/master/0020-valid-parentheses) |
<!---LeetCode Topics End-->
