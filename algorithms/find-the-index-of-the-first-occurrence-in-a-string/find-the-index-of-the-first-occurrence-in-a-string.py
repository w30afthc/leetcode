"""
title : 28. Find the Index of the First Occurrence in a String
source : https://leetcode.cn/leetbook/read/array-and-string/cm5e2/
source : https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
from typing import List


class Solution:
    """ KMP 算法，Next数组从 0 开始

    构建模式串 p 的 next 数组，记录模式串中每个位置之前位置的最长公共前后缀的长度
    在文本串 s 中寻找模式串 p，当不匹配时不用重新开始匹配
    而是查找模式串中不匹配位置的 next 的数组值，继续匹配
    时间复杂度： O(m+n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(n)
    """
    def get_next(self, p: str) -> list:
        Next = [0] * len(p)
        Next[0] = 0
        i, k = 1, 0
        while i < len(p):
            if p[i] == p[k]:
                k += 1
                Next[i] = k
                i += 1
            elif k == 0:
                Next[i] = k
                i += 1
            else:
                k = Next[k - 1]
        return Next

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        Next = self.get_next(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = Next[j - 1]

            if j == len(needle):
                return i - j
        return - 1


class Solution5:
    """KMP 算法，Next数组从 -1 开始

    构建模式串 p 的 next 数组，记录模式串中每个位置之前位置的最长公共前后缀的长度
    在文本串 s 中寻找模式串 p，当不匹配时不用重新开始匹配
    而是查找模式串中不匹配位置的 next 的数组值，继续匹配
    时间复杂度： O(m+n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(n)
    """
    def get_next(self, p: str) -> list:
        Next = [None] * len(p)
        Next[0] = -1
        i, k = 0, -1
        while i < len(p) - 1:
            if k < 0 or p[i] == p[k]:
                i += 1
                k += 1
                Next[i] = k
            else:
                k = Next[k]
        return Next

    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle):
            return -1
        Next = self.get_next(needle)
        i, j = 0, 0
        while i < len(haystack):
            if j < 0 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = Next[j]

            if j == len(needle):
                return i - j
        return -1


class Solution4:
    """字符串 find 方法

    调用字符串的 find 方法
    时间复杂度： O(m*n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        return haystack.find(needle)


class Solution3:
    """直接取索引

    直接取索引，取不到返回 -1，取到返回起始下标
    时间复杂度： O(m*n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        if needle in haystack:
            return haystack.index(needle)
        return -1


class Solution2:
    """切片比较

    分别以文本串的每个位置取长度与模式串相等长度的切片
    如果该切片与模式串相等，则返回起始位置
    时间复杂度： O(m*n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


class Solution1:
    """暴力解法

    分别以文本串的每个位置作为起始位置，依次与模式串中每个元素比较
    若相同则继续，若不同则从文本串下一个位置继续
    时间复杂度： O((m-n)*n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(1)
    """
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
    print(Solution().strStr("a", "ac"))
    print(Solution().strStr("abc", ""))
    print(Solution().strStr("", ""))
    print(Solution().strStr("", "asd"))
