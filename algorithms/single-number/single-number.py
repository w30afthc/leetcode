"""
title : 136. Single Number
source : https://leetcode.cn/problems/single-number/
"""
from typing import List


class Solution:
    """位运算

    按位异或运算^：当两个对应的二进位相异时为 1，相同时为 0
    1. 任何数和 0 做异或运算，结果仍然是原来的数，即 a ^ 0 = a
    2. 任何数和其自身做异或运算，结果是 0，即 a ^ a = 0
    3. 异或运算满足交换律和结合律，即 a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans


class Solution1:
    """暴力遍历

    取第 i 个数，看它是否在剩下的数组中
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in nums[:i] or nums[i] in nums[i+1:]:
                pass
            else:
                return nums[i]


if __name__ == "__main__":
    print(Solution().singleNumber([2,2,1]))
    print(Solution().singleNumber([4,1,2,1,2]))
    print(Solution().singleNumber([1]))
