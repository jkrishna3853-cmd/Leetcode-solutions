# 15. 3Sum

[![LeetCode Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow.svg)](https://leetcode.com/problems/3sum/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue.svg)](https://www.python.org/)

## 📜 Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

> **Note:** The solution set must **not** contain duplicate triplets.

---

## 💡 Examples

### Example 1
```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
