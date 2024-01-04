"""
source : https://leetcode.cn/problems/longest-palindromic-substring/
"""
from typing import List


class Solution:
    """
    翻转字符串，与对比原字符串的切片对比，如果相同则为回文字符串
    """
    def longestPalindrome(self, s: str) -> str:
        s_r = s[::-1]
        length = len(s)
        result = s[0]
        for i in range(length-1):
            palindromin = ""
            for j in range(i+1, length+1):
                if len(s[i:j]) > len(result) and s[i:j] == s_r[length-j:length-i]:
                    palindromin = s[i:j]
            if len(palindromin) > len(result):
                result = palindromin

        return result


class Solution1:
    """
    暴力遍历： 如果 i 位置的字符与 i + 1 或 i + 2 相同，则 i 是回文子串的中间偏左
    依次比较 i + j 与 i - j 是否相同，确定回文子串的边界
    """
    def longestPalindrome(self, s: str) -> str:
        longest_palindromin = s[0]
        length = len(s)
        for i in range(length-1):
            palindromin = ""
            if i+1 < length and s[i] == s[i+1]:
                l = min(i-0, length-i-2)
                for j in range(l+1):
                    if s[i-j] == s[i+1+j]:
                        palindromin = s[i-j:i+1+j+1]
                    else:
                        break
                if len(palindromin) > len(longest_palindromin):
                    longest_palindromin = palindromin
            if i+2 < length and s[i] == s[i+2]:
                l = min(i-0, length-i-3)
                for j in range(l+1):
                    if s[i-j] == s[i+2+j]:
                        palindromin = s[i-j:i+2+j+1]
                    else:
                        break
                if len(palindromin) > len(longest_palindromin):
                    longest_palindromin = palindromin

        return longest_palindromin


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("abbcdfffe"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("ac"))
    print(Solution().longestPalindrome("aaaa"))

