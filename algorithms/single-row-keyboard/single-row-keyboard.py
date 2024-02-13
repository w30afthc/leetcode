"""
title : 1165. Single-Row Keyboard
source : https://leetcode.cn/problems/single-row-keyboard
"""
from typing import List


class Solution:
    """模拟

    依次计算字符串 word 中每个字母与上一个字母在键盘中索引的差值
    时间复杂度： O(n), n 为字符串 word 长度
    空间复杂度： O(1)
    """
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dict = {}
        for i, key in enumerate(keyboard):
            keyboard_dict[key] = i
        ans, pre = 0, 0
        for char in word:
            index = keyboard_dict[char]
            ans += abs(index - pre)
            pre = index
        return ans


class Solution1:
    """模拟

    依次计算字符串 word 中每个字母与上一个字母在键盘中索引的差值
    时间复杂度： O(n), n 为字符串 word 长度
    空间复杂度： O(1)
    """
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_dict = dict(zip(keyboard, range(26)))
        ans = keyboard_dict[word[0]]
        for i in range(1, len(word)):
            ans += abs(keyboard_dict[word[i]] - keyboard_dict[word[i-1]])

        return ans


if __name__ == "__main__":
    print(Solution().calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba"))
    print(Solution().calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode"))
