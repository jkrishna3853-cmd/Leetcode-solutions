# 9. Palindrome Number

**Difficulty:** Easy  
**Language:** Python 3  
**Topics:** Math, Two Pointers  
**LeetCode Link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## Problem Description

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a **palindrome** when it reads the same backward as forward.

### Examples

**Example 1:**
- **Input:** `x = 121`
- **Output:** `true`
- **Explanation:** `121` reads as `121` from left to right and from right to left.

**Example 2:**
- **Input:** `x = -121`
- **Output:** `false`
- **Explanation:** From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

**Example 3:**
- **Input:** `x = 10`
- **Output:** `false`
- **Explanation:** Reads `01` from right to left. Therefore it is not a palindrome.

### Constraints
- $-2^{31} \le x \le 2^{31} - 1$

---

## Follow-up

> **Could you solve it without converting the integer to a string?**

---

## Approach & Intuition (Half-Reversal)

To solve this without string conversion or risking integer overflow, we **reverse only the second half of the number** and compare it with the first half.

### Edge Cases
1. **Negative numbers (`x < 0`):** Always `False` because of the negative sign (e.g., `-121` becomes `121-`).
2. **Numbers ending in `0`:** Always `False` (except `0` itself) because a positive multi-digit integer cannot start with `0` (e.g., `10` reverses to `01`).

### Logic
1. Extract the last digit using `x % 10`.
2. Append it to `reverted_number = reverted_number * 10 + x % 10`.
3. Divide `x` by 10 using integer division (`x //= 10`).
4. Stop when `x <= reverted_number` (half of the digits processed).
5. Compare:
   - **Even length (e.g., 1221):** `x == reverted_number` (`12 == 12`)
   - **Odd length (e.g., 121):** `x == reverted_number // 10` (`1 == 12 // 10`, middle digit removed)

---

## Step-by-Step Trace

### Trace: `x = 121` (Odd Length)
| Iteration | `x` | `reverted_number` | Loop Condition (`x > reverted_number`) |
| :---: | :---: | :---: | :---: |
| Start | `121` | `0` | `121 > 0` (True) |
| 1 | `12` | `1` | `12 > 1` (True) |
| 2 | `1` | `12` | `1 > 12` (False, Loop ends) |

- **Final Check:** `x == reverted_number // 10` $\rightarrow$ `1 == 12 // 10` $\rightarrow$ **`True`**

---

## Python 3 Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers & non-zero numbers ending in 0 cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = (reverted_number * 10) + (x % 10)
            x //= 10

        # Even length: x == reverted_number
        # Odd length:  x == reverted_number // 10
        return x == reverted_number or x == reverted_number // 10
