"""
source : https://leetcode.cn/problems/palindrome-number/description/
"""
from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Solution1:
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

