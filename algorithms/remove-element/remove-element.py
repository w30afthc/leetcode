"""
title : 27. Remove Element
source : https://leetcode.cn/problems/remove-element/
"""
from typing import List


class Solution:
    """双指针优化, 保留原数组中的元素"""
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return left


class Solution2:
    """双指针"""
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j


class Solution1:
    """相同的直接 remove """
    def removeElement(self, nums: List[int], val: int) -> int:
        i, length = 0, len(nums)
        while i < length:
            if nums[i] == val:
                nums.remove(val)
                length -= 1
            else:
                i += 1
        return length


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print(Solution().removeElement(nums, val), "nums =", nums)

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val), "nums =", nums)

    nums = [1,2,3,4]
    val = 9
    print(Solution().removeElement(nums, val), "nums =", nums)

    nums = []
    val = 9
    print(Solution().removeElement(nums, val), "nums =", nums)

    nums = [1]
    val = 1
    print(Solution().removeElement(nums, val), "nums =", nums)
