---
layout: post
title:  "合并K个排序链表"
author: Harry
---

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
```
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
```

Link: https://leetcode.com/problems/merge-k-sorted-lists

## 思路
归并排序


## 代码
MergeSort
```python
# Python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[ListNode], l: int, r: int):
        if l > r:
            return None
        if l == r:
            return lists[l]
        if l + 1 == r:
            return self.mergeTwoLists(lists[l], lists[r])

        m = l + (r - 1) / 2

        l1 = self.merge(lists, l, m)
        l2 = self.merge(lists, m + 1, r)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
                swap(l1, l2)
            tail.next = l1
            l1 = l1.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next
```
