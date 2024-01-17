"""
title : 9. Palindrome Number
source : https://leetcode.cn/problems/palindrome-number/
"""
from typing import List


class Solution:
    """数字转字符串

    将数字转为字符串，翻转字符串得出结论
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Solution1:
    """数学

    将每个位置的数字追加到列表中，对比列表翻转前后是否相同得出结论
    时间复杂度： O(log n)
    空间复杂度： O(log n)
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        n = 0
        num_list = []
        while x >= 10**n:
            num_list.append(x//10**n - x//10**(n+1)*10)
            n += 1
        if num_list == num_list[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
