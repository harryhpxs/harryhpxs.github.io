---
layout: post
title:  "二叉树中的最大路径和"
author: Harry
---

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]
```
   1
  / \
 2   3
```
输出: 6

示例 2:

输入: [-10,9,20,null,null,15,7]
```
   -10
   / \
  9  20
    /  \
   15   7
```
输出: 42

Link: https://leetcode.com/problems/binary-tree-maximum-path-sum


## 思路
待补充...

## 代码
```python
# Python 3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        self._maxPathSum(root)
        return self.maxSum

    def _maxPathSum(self, root):
        if root is None:
            return 0
        left = self._maxPathSum(root.left)
        right = self._maxPathSum(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxSum = max(self.maxSum, root.val + left + right)
        return max(left, right) + root.val
```
Ref: https://shenjie1993.gitbooks.io/leetcode-python/124%20Binary%20Tree%20Maximum%20Path%20Sum.html
