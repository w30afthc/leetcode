"""
title : 283. Move Zeroes
source : https://leetcode.cn/leetbook/read/array-and-string/c6u02/
source : https://leetcode.cn/leetbook/read/sort-algorithms/evfj1d/
source : https://leetcode.cn/problems/move-zeroes/
"""
from typing import List
from collections import deque


class Solution:
    """双指针

    快指针遇到非零则与慢指针交换值，遇到 0 跳过
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if slow < fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1


class Solution2:
    """冒泡法

    如果当前位置为 0 ，且下一个位置不是 0，则交换位置
    每次循环将一个 0 挪至最后一位
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if nums[j] == 0 and nums[j + 1] != 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


class Solution1:
    """暴力解法

    遇到 0 直接移到队尾
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums) - 1
        while i < n:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                n -= 1
                i += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)

    nums = [0]
    Solution().moveZeroes(nums)
    print(nums)

    nums = [0,1,-1]
    Solution().moveZeroes(nums)
    print(nums)

    nums = [0, 0, -1]
    Solution().moveZeroes(nums)
    print(nums)
