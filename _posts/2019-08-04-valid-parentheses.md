---
layout: post
title:  "Valid Parentheses 有效括号"
author: Harry
---

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

- 左括号必须用相同类型的右括号闭合。
- 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

Link: https://leetcode.com/problems/valid-parentheses


## 思路
利用栈的特性，去存储当前字符串中的左括号。
当遍历到右括号时，pop出栈顶与该右括号验证是否闭合。

若不能闭合，返回False；若能闭合，遍历至字符串最后一位，最终查看栈中左括号是否全部pop出。

Note: 输入字符串长度必须为偶数，否则直接返回False。若第一个字符为右括号，直接返回False。

## 代码
```python
# Python 3
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        leftP = ['(', '[', '{']
        leftStack = []
        for c in s:
            if not leftStack:
                if c in leftP:
                    leftStack.append(c)
                else:
                    return False
            else:
                if c in leftP:
                    leftStack.append(c)
                else:
                    if (c == ')' and leftStack[-1] == '(') or \
                       (c == ']' and leftStack[-1] == '[') or \
                       (c == '}' and leftStack[-1] == '{'):
                        leftStack.pop()
                    else:
                        return False
        return False if leftStack else True
```

## Follow-up
1. 若允许更多不同字符存在，如何更高效地验证成对闭合？（目前方法与允许字符数量相关）
