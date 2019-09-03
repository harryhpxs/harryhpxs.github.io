---
layout: post
title:  "53. 最大子序和"
author: Harry
---

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

Link: https://leetcode.com/problems/maximum-subarray


## 思路

#### 1. 动态计算当前最大子数组和 O(n)
遍历数组，并记录最大的sum。
- 若当前的sum > 0，则继续加上下一元素
    - 因为此时的sum对后面的sum有积极作用
- 否则，设sum为下一元素
    - 若sum为非正数，对后一位sum无积极作用，故舍去


#### 2. 分治法 O(nlogn)
待补充...


## 代码

```python
# Python 3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for i in nums[1:]:
            if currSum > 0:
                currSum += i
            else:
                currSum = i
            if maxSum < currSum:
                maxSum = currSum

        return maxSum
```
