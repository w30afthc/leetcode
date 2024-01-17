"""
title : 153. Find Minimum in Rotated Sorted Array
source : https://leetcode.cn/leetbook/read/array-and-string/c3ki5/
source : https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array
"""
from typing import List


class Solution:
    """二分查找

    思路说明
    时间复杂度： O(log n)
    空间复杂度： O(1)
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    print(Solution().findMin([3,4,5,1,2]))
    print(Solution().findMin([4,5,6,7,0,1,2]))
    print(Solution().findMin([11,13,15,17]))
    print(Solution().findMin([12]))
