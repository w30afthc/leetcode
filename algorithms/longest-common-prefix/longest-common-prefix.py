"""
source : https://leetcode.cn/problems/longest-common-prefix/description/
"""
from typing import List


class Solution:
    """将字符串数组中所有子串纵向打包，再集合去重，长度为 1 的是公共部分"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for elem in list(map(set, zip(*strs))):
            if len(elem) == 1:
                prefix += elem.pop()
            else:
                break

        return prefix


class Solution6:
    """二分查找"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def is_common_prefix(index):
            str0, count = strs[0], len(strs)
            return all(str0[:index+1] == strs[i][:index+1] for i in range(1, count))

        low, high = 0, min(len(substr) for substr in strs) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if is_common_prefix(mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:low]


class Solution5:
    """分治"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end) -> str:
            if start == end:
                return strs[start]

            middle = (start + end) // 2
            leftstr, rightstr = lcp(start, middle), lcp(middle + 1, end)
            length = min(len(leftstr), len(rightstr))
            for i in range(min(len(leftstr), len(rightstr))):
                if leftstr[i] != rightstr[i]:
                    return leftstr[:i]

            return leftstr[:length]

        return lcp(0, len(strs) - 1)


class Solution4:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
            # if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
            #     return strs[0][:i]

        return strs[0]


class Solution3:
    """
    取两个子串的最长公共前缀，作为新的子串依再次与下一个子串比较
    直到遍历完所有子串或最长公共前缀为空
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            if not prefix:
                break
            prefix = self.lcp(prefix, strs[i])
        return prefix

    def lcp(self, str1, str2):
        index, lenght = 0, min(len(str1), len(str2))
        while index < lenght:
            if str1[index] == str2[index]:
                index += 1
            else:
                break
        return str1[:index]


class Solution2:
    """
    给字符串数组排序，排序后只要比较首尾两个子串的相同前缀即可
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort()
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                return prefix
        return prefix


class Solution1:
    """
    只检查最短子字符串长度个字符
    依次取首个子字符串的字符，与其它子字符串对应位置的字符比较
    如果全部相同则追加到最长公共前缀中，否则返回结果
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substr_min_length = min(len(substr) for substr in strs)
        prefix = ""
        for j in range(substr_min_length):
            for i in range(len(strs)):
                if strs[0][j] != strs[i][j]:
                    return prefix
            prefix += strs[0][j]
        return prefix


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))
    print(Solution().longestCommonPrefix(["",""]))
    print(Solution().longestCommonPrefix(["abc",""]))
    print(Solution().longestCommonPrefix(["ab", "a"]))
    print(Solution().longestCommonPrefix(["ab", "c"]))
    print(Solution().longestCommonPrefix(["abc"]))


