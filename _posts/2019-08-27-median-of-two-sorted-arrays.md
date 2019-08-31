---
layout: post
title:  "4. 寻找两个有序数组的中位数"
author: Harry
---

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
```
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
```
示例 2:
```
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
```

Link: https://leetcode.com/problems/median-of-two-sorted-arrays


## 思路
Ref: https://www.youtube.com/watch?v=LPFhl65R7ww

时间复杂度为 O(log(min(m,n)))

中位数位于两数组合并后的中部位置，奇数长度为中间元素，偶数长度为中间两元素之平均值

如：[1,3,5] [2,3] -> 3 (奇) *或* [1,3,5] [2,4,6] -> (3+4)/2 = 3.5 (偶)

对较短数组X作二分查找，先从其中间开始切开。

另一数组Y切开位置为 (合并数组长度一半 - 较短数组长度一半)

若该分割，无法获取合理的数组X与数组Y左右部分，即：
- XLeftMax <= YRightMin 和 YLeftMax <= XRightMin

便重新分割数组X和数组Y，切割位置根据先前情况左右移动。

## 代码

```python
# Python 3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        # Keep the shorter list at first
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        """
        # Special case 1: the shorter list is empty
        if len1 == 0:
            if len2 % 2 == 0:
                return (nums2[int(len2/2)-1] + nums2[int(len2/2)]) / 2
            else:
                return nums2[int(len2/2)]
        """
        lenT = len1 + len2

        l = 0
        r = len1

        while l <= r:
            partX = int((l+r)/2)
            partY = int((lenT+1)/2) - partX

            XLeftMax = float('-inf') if partX == 0 else nums1[partX-1]
            XRightMin = float('inf') if partX == len1 else nums1[partX]
            YLeftMax = float('-inf') if partY == 0 else nums2[partY-1]
            YRightMin = float('inf') if partY == len2 else nums2[partY]

            if XLeftMax <= YRightMin and YLeftMax <= XRightMin:
                if lenT % 2 == 0:
                    leftMax = max(XLeftMax, YLeftMax)
                    rightMin = min(XRightMin, YRightMin)
                    return (leftMax + rightMin) / 2
                else:
                    return max(XLeftMax, YLeftMax)
            elif YLeftMax > XRightMin:
                l = partX + 1
            else:
                r = partX - 1
```
