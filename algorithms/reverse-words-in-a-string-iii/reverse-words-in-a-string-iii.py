"""
title : 557. Reverse Words in a String III
source : https://leetcode.cn/leetbook/read/array-and-string/c8su7/
source : https://leetcode.cn/problems/reverse-words-in-a-string-iii/
"""
from typing import List
from collections import deque


class Solution:
    """双端队列

    字母头部插入，单词尾部追加
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def reverseWords(self, s: str) -> str:
        ans = ""
        word = ""
        for i in range(len(s)):
            if s[i] != " ":
                word = s[i] + word
            else:
                ans = ans + word + " "
                word = ""
        ans = ans + word
        return ans


class Solution1:
    """常规思路

    分割、翻转、再连接
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list = [word[::-1] for word in s_list]
        return " ".join(s_list)


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))
    print(Solution().reverseWords("Mr Ding"))
    print(Solution().reverseWords("A"))
