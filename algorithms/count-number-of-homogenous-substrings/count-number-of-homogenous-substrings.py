"""
title : 1759. Count Number of Homogenous Substrings
source : https://leetcode.cn/problems/count-number-of-homogenous-substrings/
"""
from typing import List


class Solution:
    """分组循环

    慢指针指向同质字符串的开始，快指针试探同质字符串的结束
    同质字符串的个数等于：快指针 - 慢指针 + 1 的累加
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def countHomogenous(self, s: str) -> int:
        i, n = 0, len(s)
        count = 0
        while i < n:
            start = i
            while i < n and s[start] == s[i]:
                i += 1
                count += i - start
        return count % (10 ** 9 + 7)


class Solution1:
    """双指针

    慢指针指向同质字符串的开始，快指针试探同质字符串的结束
    同质字符串的个数等于：快指针 - 慢指针 + 1 的累加
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def countHomogenous(self, s: str) -> int:
        count = 0
        slow = 0
        for fast in range(len(s)):
            if s[slow] != s[fast]:
                slow = fast
            count += fast - slow + 1
        return count % int(1e9 + 7)


if __name__ == "__main__":
    print(Solution().countHomogenous(s="abbcccaa"))
    print(Solution().countHomogenous(s="xy"))
    print(Solution().countHomogenous(s="zzzzz"))
