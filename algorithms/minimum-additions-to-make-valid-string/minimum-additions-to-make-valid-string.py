"""
title : 2645. Minimum Additions to Make Valid String
source : https://leetcode.cn/problems/minimum-additions-to-make-valid-string/
"""
from typing import List


class Solution:
    """贪心

    依次遍历字符串的每个元素，判断当前字母是否是abc
    如果不是则需要插入一个字母，如果是则判断下一个元素
    最后一个字母需要额外处理一下
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def addMinimum(self, word: str) -> int:
        i, j, result = 0, 0, 0
        while i < len(word):
            if ord(word[i]) - ord("a") == j:
                i += 1
            else:
                result += 1
            j = (j + 1) % 3
        return result + (3 - j) % 3


class Solution5:
    """计算组数

    需要插入的字母总数 = 插入字母后有效abc子串数 * 3 - 原始字符串长度
    如果当前字母大于前一个字母，则它们在同一个子串中，否则在不同的子串中
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def addMinimum(self, word: str) -> int:
        n, count = len(word), 1
        for i in range(1, n):
            if word[i - 1] >= word[i]:
                count += 1
        return count * 3 - n


class Solution4:
    """直接拼接

    ord("a") = 97, ord("b") = 98, ord("c") = 99
    如果当前字母与前一个字母差值为 1 或 -2 ，则当前位置与前一个位置之间不需要插入字母
    如果差 2 或 -1 则需要插入 1 个字母，如果差 0 则需要插入 2 个字母
    头尾两个字母需要额外处理
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def addMinimum(self, word: str) -> int:
        n = len(word)
        result = ord(word[0]) - ord("a") + ord("c") - ord(word[-1])
        for i in range(1, n):
            result += (ord(word[i]) - ord(word[i-1]) - 1 + 3) % 3
        return result


class Solution3:
    """动态规划

    状态数组 d[i] 表示到 i 个元素为止需要插入字母数
    如果 word[i-1] < word[i] (即ab,ac,bc)，则插入的字母总数可以少一个
    如果 word[i-1] >= word[i] ，则需要插入两个字母
    时间复杂度： O(n)
    空间复杂度： O(n)，只用到状态数组的最后一位，可以降低到 O(1)
    """
    def addMinimum(self, word: str) -> int:
        n = len(word)
        d = [0] * n
        d[0] = 2
        for i in range(1, n):
            if word[i] > word[i - 1]:
                d[i] = d[i - 1] - 1
            else:
                d[i] = d[i - 1] + 2
        return d[n - 1]


class Solution2:
    """哈希表

    构建每种字母组号和要插入的字母数的哈希表
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def addMinimum(self, word: str) -> int:
        d = {
            "abc": 0,
            "ab": 1,
            "ac": 1,
            "bc": 1,
            "a": 2,
            "b": 2,
            "c": 2,
        }
        i, count = 0, 0
        n = len(word)
        while i < n:
            for j in [3, 2, 1]:
                if word[i:i + j] in d:
                    count += d[word[i:i + j]]
                    i += j
                    break
        return count


class Solution1:
    """暴力遍历

    依次判断字符串中的字符，视其前后情况插入0-2个字母
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def addMinimum(self, word: str) -> int:
        i, count = 0, 0
        length = len(word)
        while i < length:
            if word[i] == "c":
                count += 2
            elif word[i] == "b":
                if length - i > 1 and word[i + 1] == "c":
                    count += 1
                    i += 1
                else:
                    count += 2
            else:
                if length - i > 1:
                    if word[i + 1] == "c":
                        count += 1
                        i += 1
                    elif word[i + 1] == "b":
                        if length - i > 2 and word[i + 2] == "c":
                            i += 2
                        else:
                            count += 1
                            i += 1
                    else:
                        count += 2
                else:
                    count += 2
            i += 1
        return count


if __name__ == "__main__":
    print(Solution().addMinimum("b"))
    print(Solution().addMinimum("aaa"))
    print(Solution().addMinimum("abc"))
