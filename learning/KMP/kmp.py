"""
KMP : Knuth–Morris–Pratt（KMP）算法是一种改进的字符串匹配算法，
它的核心是利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的。
它的时间复杂度是 O(m+n)O(m + n)O(m+n)。
source : https://leetcode.cn/leetbook/read/array-and-string/cpoo6/
"""


class Solution:
    """KMP算法

    构建模式串 p 的 next 数组，记录模式串中每个位置之前位置的最长公共前后缀的长度
    在文本串 s 中寻找模式串 p，当不匹配时不用重新开始匹配
    而是查找模式串中不匹配位置的 next 的数组值，继续匹配
    时间复杂度： O(m+n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(n)
    """
    def build_next(self, p: str) -> list:
        next = [None] * len(p)
        next[0] = -1
        i, j = 0, -1
        while i < len(p) - 1:
            if j < 0 or p[i] == p[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]

        return next

    def kmp(self, s: str, p: str) -> int:
        next = self.build_next(p)
        i, j = 0, 0
        while i < len(s):
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]

            if j == len(p):
                return i - j
        return -1


class Solution1:
    """通用暴力解法

    分别以文本串的每个位置作为起始位置，依次与模式串中每个元素比较
    若相同则继续，若不同则从文本串下一个位置继续
    时间复杂度： O(m*n), m为文本串s的长度，n为模式串p的长度
    空间复杂度： O(1)
    """
    def kmp(self, s: str, p: str) -> int:
        i, j = 0, 0
        while i <= len(s) - len(p):
            while j < len(p):
                if s[i+j] == p[j]:
                    j += 1
                else:
                    j = 0
                    break
            if j == len(p):
                return i

            i += 1

        return -1


if __name__ == "__main__":
    print(Solution().kmp("AAAAAAAG", "AAAAG"))
    print(Solution().kmp("ACTGPACTGKACTGPACY", "ACTGPACY"))
    print(Solution().kmp("AAG", "AAG"))
    print(Solution().kmp("AG", "AAG"))
