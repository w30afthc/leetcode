"""
title : 1446. Consecutive Characters
source : https://leetcode.cn/problems/consecutive-characters/
"""
from typing import List


class Solution:
    """双指针

    慢指针记录相同子串的开始位置，快指针记录结束位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def maxPower(self, s: str) -> int:
        slow, ans = 0, 1
        for fast in range(len(s)):
            if s[slow] == s[fast]:
                ans = max(ans, fast - slow + 1)
            else:
                slow = fast
        return ans


class Solution1:
    """分组循环

    外层循环记录子串开始位置，内层循环记录结束位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def maxPower(self, s: str) -> int:
        max_power = -1
        i, n = 0, len(s)
        while i < n:
            character_index = i
            i += 1
            while i < n and s[character_index] == s[i]:
                i += 1
            max_power = max(max_power, i - character_index)
        return max_power


if __name__ == "__main__":
    print(Solution().maxPower("leetcode"))
    print(Solution().maxPower("abbcccddddeeeeedcba"))
    print(Solution().maxPower("a"))
