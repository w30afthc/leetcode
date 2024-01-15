"""
title : 20. Valid Parentheses
source : https://leetcode.cn/problems/valid-parentheses
"""
from typing import List
from collections import deque


class Solution:
    """堆栈

    奇数长度一定的字符串一定无效
    采用哈希表（字典）加快判断
    时间复杂度： O(n)
    空间复杂度： O(n+∣Σ∣), 其中 Σ 表示字符集，本题中字符串只包含 6 种括号，∣Σ∣=6。
    栈中的字符数量为 O(n)，而哈希表使用的空间为 O(∣Σ∣)，相加即可得到总空间复杂度
    """
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        d = {")": "(", "]": "[", "}": "{"}
        l = []
        for i in s:
            if i not in d:
                l.append(i)
            elif l and l[-1] == d[i]:
                l.pop()
            else:
                return False
        return False if l else True


class Solution1:
    """堆栈

    遇左括号则入栈，遇右括号则判断栈顶是否为对应的左括号
    是则出栈，否则返回 False
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        d = deque()
        for ele in s:
            if ele in "([{":
                d.append(ele)
            elif ele == ")" and len(d) and d[-1] == "(":
                d.pop()
            elif ele == "]" and len(d) and d[-1] == "[":
                d.pop()
            elif ele == "}" and len(d) and d[-1] == "{":
                d.pop()
            else:
                return False
        return False if len(d) else True


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("[])"))
