"""
title : 1. Two Sum
source : https://leetcode.cn/problems/two-sum/
"""
from typing import List


class Solution:
    """哈希表

    对于数组中的每个数，如果该数与目标值的差值不在哈希表中，则添加该数与对应下标哈希表中
    如果在哈希表中则返回差值对应的下标和当前数的下标
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


class Solution2:
    """暴力枚举

    对于数组中的每个数，计算 target - 该数后是否在剩下的数组切片中
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target-nums[i], i+1)]


class Solution1:
    """暴力枚举

    对于数组中的每个数，遍历另一个数使两者之和为 target
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
    print(Solution().twoSum([0, 0, 3, 4], 0))
