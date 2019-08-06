---
layout: post
title:  "数组中第k大元素"
author: Harry
---

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
```
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
```
示例 2:
```
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```
说明:

可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

Link: https://leetcode.com/problems/kth-largest-element-in-an-array

## 思路
One line: 先排序，再指向倒数第k个数

Quicksort: 基于快排使用基准数去找出第k大的数

Heap: 待续...


## 代码
One line - O(n log n)
```python
# Python 3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
```

Quicksort
```python
# Python 3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.getKth(nums, len(nums)-k+1, 0, len(nums)-1)

    def getKth(self, nums: List[int], k: int, start: int, end: int) -> int:
        pivot = nums[end]
        left = start
        right = end

        while True:
            while nums[left] < pivot and left < right:
                left += 1
            while nums[right] >= pivot and right > left:
                right -= 1
            if left == right:
                break
            self.swap(nums, left, right)

        self.swap(nums, left, end)

        if k == left + 1:
            return pivot
        elif k < left + 1:
            return self.getKth(nums, k, start, left - 1)
        else:
            return self.getKth(nums, k, left + 1, end)

    def swap(self, nums: List[int], a: int, b: int) -> None:
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
```
