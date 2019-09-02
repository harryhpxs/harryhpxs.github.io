---
layout: post
title:  "26. 删除排序数组中的重复项"
author: Harry
---

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
```
给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
```
示例 2:
```
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
```
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:
```java
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array


## 思路

### Java 思路

遍历数组，当下一元素与当前元素相同，继续循环记录重复元素数量；若不同，则把下一元素改为之后第一个不同元素。

若出现下一元素比当前元素小的情况，因为之前的操作使更大元素被写入当前元素cell；此时需要把接下来后面的更小元素修改为当前元素，直到找到更大元素。

最后，若当前元素与数组最后(最大)元素相等，则完成。

### Python 思路

直接修改list，当遇到重复元素时，对原list进行删除操作(del)。可再细分至以下两种写法：
1. 遇到一个重复就删除一个；
2. 数出后面所有重复元素个数，通过切片(slice)一并删除。


## 代码

```java
// Java
class Solution {
    public int removeDuplicates(int[] nums) {
        int len = 0, dupCount = 0, curr;

        for (int i = 0; i < nums.length; i++) {
            len++;
            curr = nums[i];
            dupCount = 0;

            // 若当前元素与最后(最大)元素相等，则完成
            if (curr == nums[nums.length-1]) {
                break;
            }

            for (int j = i + 1; j < nums.length; j++) {
                if (curr < nums[j]) {
                    break;
                } else {
                    nums[j] = curr;
                    dupCount++;
                }
            }
            nums[i+1] = nums[i+1+dupCount];
        }
        return len;
    }
}
```

```python
# Python 3
# Solution 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                del nums[i]
            i += 1

        return len(nums)
```

```python
# Python 3
# Solution 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        dupCount = 0

        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    dupCount += 1
                    j += 1
                else:
                    break
            del nums[i:i+dupCount]
            i += 1
            dupCount = 0

        return len(nums)
```
