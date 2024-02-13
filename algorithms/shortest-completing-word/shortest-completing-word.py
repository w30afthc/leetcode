"""
title : 748. Shortest Completing Word
source : https://leetcode.cn/problems/shortest-completing-word/
"""
from typing import List
from collections import Counter


class Solution:
    """模拟

    先统计 licensePlate 中字母词频，再遍历字符串数组，依次统计各个字符串的词频
    利用 Counter 对象相减能选出补全词，再挑选长度最短的
    时间复杂度： O(n + l + m * 26), n 为 licensePlate 长度，l 为 words 中的是所有字符串长度之和
    m 为 words 数组的长度
    空间复杂度： O(26)
    """
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)


class Solution1:
    """模拟

    先统计 licensePlate 中字母词频，然后遍历字符串数组中每个字符串
    如果存在于列表 license_list 则删除，对于能清空词频列表的字符串，选出最短的
    时间复杂度： O(n * m), n 为 licensePlate 长度，m 为 words
    空间复杂度： O(n)
    """
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        shortest = "a" * 16
        license_list = []
        for char in licensePlate:
            if char.isalpha():
                license_list.append(char.lower())
        for word in words:
            temp_list = license_list[:]
            for char in word:
                if not temp_list:
                    break
                if char in temp_list:
                    temp_list.pop(temp_list.index(char))
            if not temp_list and len(word) < len(shortest):
                shortest = word
        return shortest


if __name__ == "__main__":
    print(Solution().shortestCompletingWord(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]))
    print(Solution().shortestCompletingWord(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"]))
    print(Solution().shortestCompletingWord(licensePlate="Ah71752", words=["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))
