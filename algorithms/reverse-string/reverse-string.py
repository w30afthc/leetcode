"""
source : https://leetcode.cn/problems/reverse-string/solution/
"""
from typing import List


class Solution:
    """双指针"""
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class Solution1:
    """python 库函数解法

    s[:] = s[::-1] 是切片赋值语法，表示用 s[::-1] 替换 s 中的元素。
    注意不能写成 s = s[::-1]，因为 s 只是一个局部变量，
    对它的修改不会影响到函数外部传入的实际参数。
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    print(s)

    s = ["H","a","n","n","a","h"]
    Solution().reverseString(s)
    print(s)

    s = ["a"]
    Solution().reverseString(s)
    print(s)

    s = ["a", "b"]
    Solution().reverseString(s)
    print(s)
