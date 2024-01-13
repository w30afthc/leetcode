"""
title : 35. Search Insert Position
source : https://leetcode.cn/leetbook/read/array-and-string/cxqdh/
source : https://leetcode.cn/problems/search-insert-position/
"""
from typing import List


class Solution:
    """二分法

    左右指针的均值与目标值对比，调整左右指针位置
    如果数组中存在目标值，则最终 均值 = 目标值
    如果不存在，插入位置为 left
    时间复杂度： O(log n)
    空间复杂度： O(1)
    """
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
    """二分法

    左右指针的均值与目标值对比，调整左右指针位置
    如果数组中存在目标值，则最终 均值 = 目标值
    如果不存在，插入位置为 left
    时间复杂度： O(log n)
    空间复杂度： O(1)
    """
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
    """常规遍历

    遍历数组，找到大于等于目标值的位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
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
