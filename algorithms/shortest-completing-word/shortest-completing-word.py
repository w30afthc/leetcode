"""
title : 748. Shortest Completing Word
source : https://leetcode.cn/problems/shortest-completing-word/
"""
from typing import List


class Solution:
    """模拟

    思路说明
    时间复杂度： O(n)
    空间复杂度： O(1)
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
