# 13. Roman to Integer

[![LeetCode Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen.svg)](https://leetcode.com/problems/roman-to-integer/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue.svg)](https://www.python.org/)

## 📜 Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`.

| Symbol | Value |
| :---: | :---: |
| **I** | 1 |
| **V** | 5 |
| **X** | 10 |
| **L** | 50 |
| **C** | 100 |
| **D** | 500 |
| **M** | 1000 |

Roman numerals are usually written largest to smallest from left to right. However, six instances use subtraction rules:
* `I` before `V` (5) and `X` (10) makes **4** and **9**.
* `X` before `L` (50) and `C` (100) makes **40** and **90**.
* `C` before `D` (500) and `M` (1000) makes **400** and **900**.

Given a valid Roman numeral string `s`, convert it to an integer.

---

## 💡 Examples

### Example 1
```text
Input: s = "III"
Output: 3
Explanation: III = 3
