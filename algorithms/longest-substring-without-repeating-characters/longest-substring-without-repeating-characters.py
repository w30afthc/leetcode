"""
title : 3. Longest Substring Without Repeating Characters
source : https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""
from typing import List


class Solution:
    """哈希表

    哈希表（字典）中键值对记录每个字符出现在字符串中的位置
    右指针遍历字符串，当有重复字符时更新左指正的位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = -1, 0
        hashtable = {}
        for right in range(len(s)):
            if s[right] in hashtable:
                left = max(left, hashtable[s[right]])
            hashtable[s[right]] = right
            result = max(result, right - left)
        return result


class Solution1:
    """双指针

    左指针记录无重复字符的开始，右指针试探无重复字符的结束
    当有重复字符字符时，左指针指向重复字符的下一个位置
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0, 0
        for right in range(len(s)):
            if s[right] in s[left:right]:
                left = s.index(s[right], left) + 1
            else:
                result = max(result, right - left + 1)
        return result


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
    print(Solution().lengthOfLongestSubstring(s="b"))
    print(Solution().lengthOfLongestSubstring(s="pwwkew"))
    print(Solution().lengthOfLongestSubstring(s="bbtablud"))
