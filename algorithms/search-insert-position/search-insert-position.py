"""
source : https://leetcode.cn/problems/search-insert-position/description/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return left


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = (left + right) // 2
        while left <= right:
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                return index
            index = (left + right) // 2
        return index + 1


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 0))
    print(Solution().searchInsert([1,3,5,6], 1))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 3))
    print(Solution().searchInsert([1,3,5,6], 4))
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 6))
    print(Solution().searchInsert([1,3,5,6], 7))

