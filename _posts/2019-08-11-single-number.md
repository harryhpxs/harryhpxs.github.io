---
layout: post
title:  "只出现一次的数字"
author: Harry
---

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
```
输入: [2,2,1]
输出: 1
```
示例 2:
```
输入: [4,1,2,1,2]
输出: 4
```

Link: https://leetcode.com/problems/single-number


## 思路
1. 使用set()求当前nums中所有不同元素之和，其两倍减去nums得出只出现一次的数字。
2. Bitwise operation 待补充...


## 代码
```python
# Python 3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
```
