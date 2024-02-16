"""
title : 3. Longest Substring Without Repeating Characters
source : https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""
from typing import List


class Solution:
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
    print(Solution().lengthOfLongestSubstring(s="bbbbb"))
    print(Solution().lengthOfLongestSubstring(s="pwwkew"))
    print(Solution().lengthOfLongestSubstring(s="bbtablud"))
