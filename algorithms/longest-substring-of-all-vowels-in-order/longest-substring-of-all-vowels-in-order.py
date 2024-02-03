"""
title : 1839. Longest Substring Of All Vowels in Order
source : https://leetcode.cn/problems/longest-substring-of-all-vowels-in-order/
"""
from typing import List
import re


class Solution4:
    """正则表达式

    正则表达式
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestBeautifulSubstring(self, word: str) -> int:
        result = 0
        matches = re.finditer(r"a+e+i+o+u+", word)
        for match in matches:
            result = max(result, len(match.group()))
        return result


class Solution3:
    """模拟

    找出所有相同的连续字符，如果字符是满足 "aeiou" 顺序，则计算长度并累加
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestBeautifulSubstring(self, word: str) -> int:
        length, answer = 0, 0
        cur, vowels = 0, "aeiou"
        i, n = 0, len(word)
        while i < n:
            start = i
            while i < n and word[start] == word[i]:
                i += 1

            if word[start] != vowels[cur]:
                cur, length = 0, 0
                if word[start] != vowels[0]:
                    continue

            length += i - start
            cur += 1
            if cur == 5:
                answer = max(answer, length)
                cur, length = 0, 0
        return answer


class Solution:
    """分组循环

    外循环找到美丽子字符串的开始（即首个 "a" 的位置），内循环试探美丽子字符串的结尾
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestBeautifulSubstring(self, word: str) -> int:
        i, n = 0, len(word)
        result = 0
        vowels_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        while i < n:
            if word[i] != "a":
                i += 1
                continue
            start = i
            i += 1
            while i < n and (word[i-1] == word[i] or vowels_dict[word[i-1]] + 1 == vowels_dict[word[i]]):
                if word[i] == "u":
                    result = max(result, i - start + 1)
                i += 1
        return result


class Solution1:
    """双指针

    慢指针指向字符 "a", 快指针试探美丽子字符串的结尾
    快指针试探时得满足当前字符等于前一个字符或只比前一个字符大一位
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestBeautifulSubstring(self, word: str) -> int:
        slow, result = 0, 0
        vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        for fast in range(1, len(word)):
            if word[slow] == "a" and (word[fast - 1] == word[fast] or \
                                      vowels[word[fast - 1]] + 1 == vowels[word[fast]]):
                if word[fast] == "u":
                    result = max(result, fast - slow + 1)
            else:
                slow = fast
        return result


if __name__ == "__main__":
    print(Solution().longestBeautifulSubstring(word="aeiaaioaaaaeiiiiouuuooaauuaeiu"))
    print(Solution().longestBeautifulSubstring(word="aeeeiiiioooauuuaeiou"))
    print(Solution().longestBeautifulSubstring(word="a"))
