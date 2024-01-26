"""
title : 1869. Longer Contiguous Segments of Ones than Zeros
source : https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/
"""
from typing import List


class Solution:
    """分组循环

    外循环记录连续子字符串开始位置，内循环记录连续子字符串结束位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def checkZeroOnes(self, s: str) -> bool:
        max_zeros, max_ones = 0, 0
        i, n = 0, len(s)
        while i < n:
            start = i
            i += 1
            while i < n and s[start] == s[i]:
                i += 1
            if s[start] == "0":
                max_zeros = max(max_zeros, i - start)
            else:
                max_ones = max(max_ones, i - start)
        return max_ones > max_zeros


class Solution1:
    """双指针

    慢指针指向连续子字符串的开始，快指针指向连续子字符串的结束
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def checkZeroOnes(self, s: str) -> bool:
        max_zeros, max_ones = 0, 0
        slow, fast, n = 0, 0, len(s)
        while fast < n:
            if s[slow] == s[fast]:
                if s[slow] == "0":
                    max_zeros = max(max_zeros, fast - slow + 1)
                else:
                    max_ones = max(max_ones, fast - slow + 1)
            else:
                slow = fast
                fast -= 1
            fast += 1
        return max_ones > max_zeros


if __name__ == "__main__":
    print(Solution().checkZeroOnes("1101"))
    print(Solution().checkZeroOnes("111000"))
    print(Solution().checkZeroOnes(s="110100010"))
    print(Solution().checkZeroOnes(s="1"))
