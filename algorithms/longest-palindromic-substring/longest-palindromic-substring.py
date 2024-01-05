"""
source : https://leetcode.cn/problems/longest-palindromic-substring/
"""
from typing import List


class Solution:
    """the fastest solution"""
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(i - len(res) - 1, 0)
            temp = s[start:i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res


class Solution5:
    """Manacher Algorithms"""
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]


class Solution4:
    """中心扩展算法"""
    def center_expansion(self, s, left, right):
        while 0 <= left <= right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 1
        for i in range(len(s)):
            left1, right1 = self.center_expansion(s, i, i)
            left2, right2 = self.center_expansion(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end+1]


class Solution3:
    """动态规划"""
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1
        for L in range(2, n+1):
            for i in range(n-1):
                j = i + L - 1
                if j >= n:
                    break
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start+max_len]


class Solution2:
    """
    翻转字符串，与对比原字符串的切片对比，如果相同则为回文字符串
    """

    def longestPalindrome(self, s: str) -> str:
        s_r = s[::-1]
        length = len(s)
        result = s[0]
        for i in range(length - 1):
            for j in range(i + 1, length + 1):
                if len(s[i:j]) > len(result) and s[i:j] == s_r[length - j:length - i]:
                    result = s[i:j]

        return result


class Solution1:
    """
    暴力遍历： 如果 i 位置的字符与 i + 1 或 i + 2 相同，则 i 是回文子串的中间偏左
    依次比较 i + j 与 i - j 是否相同，确定回文子串的边界
    """

    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        length = len(s)
        for i in range(length - 1):
            if i + 1 < length and s[i] == s[i + 1]:
                n = min(i - 0, length - 1 - i - 1)
                for j in range(n + 1):
                    if s[i - j] == s[i + 1 + j]:
                        if len(s[i - j:i + 1 + j + 1]) > len(result):
                            result = s[i - j:i + 1 + j + 1]
                    else:
                        break

            if i + 2 < length and s[i] == s[i + 2]:
                n = min(i - 0, length - 1 - i - 2)
                for j in range(n + 1):
                    if s[i - j] == s[i + 2 + j]:
                        if len(s[i - j:i + 2 + j + 1]) > len(result):
                            result = s[i - j:i + 2 + j + 1]
                    else:
                        break

        return result


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("abbcdfffe"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("ac"))
    print(Solution().longestPalindrome("aaaa"))
