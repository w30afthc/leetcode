"""
source : https://leetcode.cn/problems/find-the-middle-index-in-array/
"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            if left_sum*2 + num == total:
                return i
            left_sum += num
        return -1


class Solution2:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i in range(len(nums)):
            if left_sum*2 + nums[i] == total:
                return i
            left_sum += nums[i]
        return -1


class Solution1:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


if __name__ == "__main__":
    print(Solution().findMiddleIndex([2,3,-1,8,4]))
    print(Solution().findMiddleIndex([1,-1,4]))
    print(Solution().findMiddleIndex([2,5]))
    print(Solution().findMiddleIndex([1]))
