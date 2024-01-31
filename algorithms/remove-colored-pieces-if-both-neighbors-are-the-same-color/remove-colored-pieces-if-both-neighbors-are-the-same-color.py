"""
title : 2038. Remove Colored Pieces if Both Neighbors are the Same Color
source : https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
"""
from typing import List


class Solution:
    """模拟

    遍历数组，分别计算连续 3 个 'A'和 'B' 的数量
    返回数量比较结果即可
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1
        return alice > bob


class Solution1:
    """分组循环

    遍历数组，分别计算连续 3 个 'A'和 'B' 的数量
    返回数量比较结果即可
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def winnerOfGame(self, colors: str) -> bool:
        i, n = 0, len(colors)
        alice, bob = 0, 0
        while i < n:
            start = i
            i += 1
            while i < n and colors[start] == colors[i]:
                i += 1
            if colors[start] == "A":
                alice += max(0, i - start - 2)
            else:
                bob += max(0, i - start - 2)
        return alice > bob


if __name__ == "__main__":
    print(Solution().winnerOfGame(colors="AAABABB"))
    print(Solution().winnerOfGame(colors="AA"))
    print(Solution().winnerOfGame(colors="ABBBBBBBAAA"))
