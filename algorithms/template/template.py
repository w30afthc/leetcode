"""
source : https://leetcode.cn/problems/template/description/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            else:
                hashtable[nums[i]] = i
        else:
            return []


if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9

    # nums = [3,2,4]
    # target = 6

    nums = [3,3]
    target = 6

    print(Solution().twoSum(nums, target))

