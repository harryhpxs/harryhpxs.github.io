---
layout: post
title: "17. 电话号码的字母组合"
author: Harry
---

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

```txt
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

Link: <https://leetcode.com/problems/letter-combinations-of-a-phone-number>

## 思路

### TBW

## 代码

```python
# Python 3
class Solution:
    def __init__(self):
        self.charTable = self.setCharTable()
        
    def setCharTable(self):
        d = {}
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        return d
                
    def letterCombinations(self, digits: str) -> List[str]:
        def recCombine(currDigit, leftDigits):
            if not leftDigits:
                result.append(currDigit)
            else:
                for c in self.charTable[leftDigits[0]]:
                    recCombine(currDigit + c, leftDigits[1:])
        result = []
        if digits:
            recCombine('', digits)
        return result
```
