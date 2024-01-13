"""
title : 5. Longest Palindromic Substring
source : https://leetcode.cn/leetbook/read/array-and-string/conm7/
source : https://leetcode.cn/problems/longest-palindromic-substring/
"""
from typing import List


class Solution6:
    """翻转比较

    遍历字符串，找出比当前最长回文串还长的字符串，翻转后对比是否相同
    仅适用于 Python 代码，其它语言的字符串翻转时间复杂度为 O(n) ?
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def longestPalindrome(self, s: str) -> str:
        result = ""     # 当前循环后存在的最新的最长回文串
        # 循环遍历右下标
        for right in range(len(s)):
            # 如果存在更长回文串，则其左下标取值 left
            left = max(right - len(result) - 1, 0)
            # 可能存在的更长的回文串 temp
            temp = s[left:right + 1]
            # 回文串翻转后等于其本身
            if temp == temp[::-1]:
                # 更新最新的最长回文串（等长也更新）
                result = temp
            else:
                # left 前进一位，覆盖奇、偶数位
                temp = temp[1:]
                if temp == temp[::-1]:
                    result = temp

        return result


class Solution5:
    """ Manacher 算法

    记录之前遍历过的每个位置的最大回文串长度的一半（臂长），利用回文串左右对称，跳过当前位置不必要的计算
    如果当前位置在之前某个很长的回文串右边界（臂长）之内，找到其对称位置的臂长
    从起对称的臂长开始计算左右是否相同，以减少计算步骤
    时间复杂度： O(n)，由于对于每个位置，扩展要么从当前的最右侧臂长 right 开始
    要么只会进行一步，而 right 最多向前走 O(n) 步，因此算法的复杂度为 O(n)
    空间复杂度： O(n)
    """
    def extend(self, s, left, right):
        """给定字符串和起始位置，返回可以扩展的最大臂长"""
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        # 原字符串间插入符号，解决回文字符串奇偶问题；
        # 可以插入任意字符，不影响最终结果
        s = "#" + "#".join(s) + "#"
        # 每个位置对应的最长臂长
        arms_length = []
        # 最长回文串的起始、终点下标
        start, end = 0, -1
        # 循环查找位于 i 位置回文串时，已遍历的位置的回文中心 j 和 回文右臂能达到的最右位置 right
        j, right = -1, -1
        for i in range(len(s)):
            # 如果右臂未能覆盖，则从 0 开始检索臂长
            if i >= right:
                cur_arm_length = self.extend(s, i, i)
            else:
                # 如果右臂能覆盖，则跳过镜像位置的臂长
                i_sysmmetry = 2 * j - i
                begin_arm_length = min(arms_length[i_sysmmetry], right - i)
                cur_arm_length = self.extend(s, i - begin_arm_length, i + begin_arm_length)

            arms_length.append(cur_arm_length)

            # 如果当前位置的右臂大于之前的右臂，则更新
            if i + cur_arm_length > right:
                j, right = i, i + cur_arm_length

            # 如果当前位置的回文长度大于之前的回文，则更新
            if 2 * cur_arm_length + 1 > end - start:
                start, end = i - cur_arm_length, i + cur_arm_length

        # 因为起始和终点下标一定会落在插入的字符上，所有返回值坐标都要 +1
        # 又因为原字符间都插入了字符，所有切片步长为 2
        return s[start+1:end+1:2]


class Solution4:
    """中心扩展算法

    遍历所有可能得回文中心，尝试扩展
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
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
    """动态规划

    遍历可能得回文串长度，如果两端相等，则判断去除首位后的字符串是否是回文
    时间复杂度： O(n*n)
    空间复杂度： O(n*n)
    """
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
    """翻转字符串

    翻转后与原字符串的切片对比，如果相同则为回文字符串
    时间复杂度： O(n*n)
    空间复杂度： O(n)
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
    """暴力遍历

    如果 i 位置的字符与 i + 1 或 i + 2 相同，则 i 是回文子串的中间偏左
    依次比较 i + j 与 i - j 是否相同，确定回文子串的边界
    时间复杂度： O(n*n)
    空间复杂度： O(1)
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
