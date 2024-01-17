"""
title : 151. Reverse Words in a String
source : https://leetcode.cn/leetbook/read/array-and-string/crmp5/
source : https://leetcode.cn/problems/reverse-words-in-a-string/
"""
from typing import List
from collections import deque


class Solution:
    """拆分翻转连接

    拆分翻转连接
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution1:
    """辅助列表，正常遍历

    利用空格遍历出每个单词，放入列表头部
    最后连接单词列表
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]
            elif word:
                words.insert(0, word)
                word = ""
        if word:
            words.insert(0, word)

        return " ".join(words)


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world  "))
    print(Solution().reverseWords("a good   example"))
