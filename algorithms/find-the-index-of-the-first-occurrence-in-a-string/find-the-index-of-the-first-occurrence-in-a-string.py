"""
source : https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
from typing import List


class Solution:
    """字符串 find 方法"""
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution3:
    """直接取索引，取不到返回 -1 """
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


class Solution2:
    """切片比较"""
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


class Solution1:
    """暴力解法"""
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    pass
                else:
                    j = -1
                    break
            if j == len(needle) - 1:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().strStr("sadbutsad", "sad"))
    print(Solution().strStr("leetcode", "leeto"))
    print(Solution().strStr("ACTGPACTGKACTGPACY", "ACTGPACY"))
    print(Solution().strStr("AAG", "AAG"))
    print(Solution().strStr("abc", "c"))
