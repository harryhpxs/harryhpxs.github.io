---
layout: post
title:  "求众数"
author: Harry
---

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
```
输入: [3,2,3]
输出: 3
```
示例 2:
```
输入: [2,2,1,1,1,2,2]
输出: 2
```

Link: https://leetcode.com/problems/majority-element


## 思路
循环数组，result = None，第一个元素 -> count++。

若第二个元素与第一个相同 -> count++；否则，count--。

当count == 0, 记录当前元素为result。

由此算法得到的最终result为此数组众数。


## 代码
```python
# Python 3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = None
        count = 0
        for num in nums:
            if count == 0:
                result = num
            if result == num:
                count += 1
            else:
                count -= 1
        return result
```
