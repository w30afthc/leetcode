"""
source : https://leetcode.cn/problems/reverse-words-in-a-string/
"""
from typing import List
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution2:
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


class Solution1:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        result = " ".join(s_list[::-1])
        return result


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world  "))
    print(Solution().reverseWords("a good   example"))

