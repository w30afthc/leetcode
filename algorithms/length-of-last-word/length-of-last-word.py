"""
title : 58. Length of Last Word
source : https://leetcode.cn/problems/length-of-last-word/
"""
from typing import List


class Solution:
    """反向遍历

    从字符串末尾开始遍历，首次遇到非空格记录单词结束位置
    再次遇到空格记录单词开始位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        j = i
        while j >= 0 and s[j] != " ":
            j -= 1
        return i - j


class Solution2:
    """常规解法2

    只从右侧分割一次空格，减少需要处理的数据，加快处理速度
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit(maxsplit=1)[-1])


class Solution1:
    """常规解法

    按空格后分割，返回最后一个单词的长度
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
    print(Solution().lengthOfLastWord("a"))
