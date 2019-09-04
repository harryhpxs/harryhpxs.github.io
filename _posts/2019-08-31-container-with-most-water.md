---
layout: post
title:  "11. 盛最多水的容器"
author: Harry
---

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

<img src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" width="70%">

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:
```
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
```

Link: https://leetcode.com/problems/container-with-most-water


## 思路

#### 1. 暴力搜索 O(n<sup>2</sup>)

直接计算每一对垂直线可以容纳的水量，记录并返回最大值。**超时警告!!**


#### 2. 双向指针 O(n)

从数组两端开始往中间搜索，直线较短的指针往另一方向移动一位，记录max面积。
  - 因为只有较长直线对最大面积有帮助，故保留较长的指针，移动较短的指针

若两指针重合，搜索结束，返回max值。


## 代码

```python
# Python 3
# Solution 1 - Brute Force O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxV = 0

        for i in range(len(height)):
            x1 = i + 1
            y1 = height[i]

            for j in range(i+1, len(height)):
                x2 = j + 1
                y2 = height[j]
                v = min(y1,y2) * (x2-x1)

                if v > maxV:
                    maxV = v
        return maxV
```

```python
# Python 3
# Solution 2 - Two pointers from left and right
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxV = 0
        l = 0
        r = len(height) - 1

        while l != r:
            y1, y2 = height[l], height[r]
            v = min(y1, y2) * (r-l)
            if v > maxV:
                maxV = v

            if y1 <= y2:
                l += 1
            else:
                r -= 1

        return maxV
```
