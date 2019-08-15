---
layout: post
title:  "2的幂"
author: Harry
---

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
```
输入: 1
输出: true
解释: 2^0 = 1
```
示例 2:
```
输入: 16
输出: true
解释: 2^4 = 16
```
示例 3:
```
输入: 218
输出: false
```

Link: https://leetcode.com/problems/power-of-two


## 思路
Bitwise operation

例如：4

4 & (4-1) = 100 & (100 - 001) = 100 & 011 = 000

或者：5

5 & (5-1) = 101 & (101 - 001) = 101 & 100 = 100


## 代码
```python
# Python 3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n & (n - 1):
            return False
        else:
            return True
```
