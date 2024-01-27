"""
title : 1957. Delete Characters to Make Fancy String
source : https://leetcode.cn/problems/delete-characters-to-make-fancy-string
"""
from typing import List


class Solution:
    """模拟

    遍历原始字符串，将合适的字符添加到结果中
    如果结果字符串的最后两位与当前遍历的字符相同则跳过
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def makeFancyString(self, s: str) -> str:
        ans = []
        for character in s:
            if len(ans) >= 2 and ans[-2] == ans[-1] == character:
                continue
            ans.append(character)
        return "".join(ans)


class Solution2:
    """双指针

    外循环记录重复字符开始的位置，内循环处理重复字符
    如果第 3 个字符与前两个字符相同，则跳过重复的字符串
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def makeFancyString(self, s: str) -> str:
        ans = []
        slow = 0
        for fast in range(len(s)):
            if s[slow] == s[fast]:
                if fast - slow < 2:
                    ans.append(s[fast])
            else:
                slow = fast
                ans.append(s[fast])
        return "".join(ans)


class Solution1:
    """分组循环

    外循环记录重复字符开始的位置，内循环处理重复字符
    如果第 3 个字符与前两个字符相同，则跳过重复的字符串
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def makeFancyString(self, s: str) -> str:
        ans = []
        i, n = 0, len(s)
        while i < n:
            ans.append(s[i])
            start = i
            i += 1
            while i < n and s[start] == s[i]:
                if i - start < 2:
                    ans.append(s[i])
                i += 1
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().makeFancyString(s="leeetcode"))
    print(Solution().makeFancyString(s="aaabaaaa"))
    print(Solution().makeFancyString(s="aab"))
