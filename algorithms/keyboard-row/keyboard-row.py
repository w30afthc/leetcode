"""
title : 500. Keyboard Row
source : https://leetcode.cn/problems/keyboard-row/
"""
from typing import List


class Solution:
    """集合

    利用集合中元素不重复 + 集合包含来处理
    空间复杂度： O(n)
    """
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        row1_set = set("qwertyuiop")
        row2_set = set("asdfghjkl")
        row3_set = set("zxcvbnm")
        for word in words:
            word_set = set(word.lower())
            if word_set <= row1_set or word_set <= row2_set or word_set <= row3_set:
                ans.append(word)
        return ans


class Solution2:
    """遍历

    为每个英文字母标记其对应的键盘上的行号，然后检测字符串中所有字符对应的行号是否相同
    时间复杂度： O(n * m), n 位字符串数组长度, m 为单词平均长度
    空间复杂度： O(n)
    """
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        row_id = "12210111011122000010020202"
        for word in words:
            row = row_id[ord(word[0].lower()) - ord("a")]
            if all([row_id[ord(character.lower()) - ord("a")] == row for character in word]):
                ans.append(word)
        return ans


class Solution1:
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
