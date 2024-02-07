"""
title : 500. Keyboard Row
source : https://leetcode.cn/problems/keyboard-row/
"""
from typing import List


class Solution:
    """模拟

    依次遍历字符串数组，再遍历单词中的每个字母
    时间复杂度： O(n * m), n 位字符串数组长度, m 为单词平均长度
    空间复杂度： O(n)
    """
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            if word[0].lower() in "qwertyuiop":
                row = "qwertyuiop"
            elif word[0].lower() in "asdfghjkl":
                row = "asdfghjkl"
            else:
                row = "zxcvbnm"

            i = 1
            while i < len(word) and word[i].lower() in row:
                i += 1

            if i == len(word):
                ans.append(word)
        return ans


if __name__ == "__main__":
    print(Solution().findWords(words=["Hello","Alaska","Dad","Peace"]))
    print(Solution().findWords(words=["omk"]))
    print(Solution().findWords(words=["adsdf","sfd"]))
