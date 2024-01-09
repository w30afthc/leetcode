"""
title : 485. Max Consecutive Ones
source : https://leetcode.cn/problems/max-consecutive-ones/description/
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, slow = 0, -1
        for fast in range(len(nums)):
            if nums[fast] == 0:
                slow = fast
            if fast - slow > ans:
                ans = fast - slow
        return ans


class Solution1:
    """通用解法"""
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive, max_consecutive = 0, 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                max_consecutive = max(consecutive, max_consecutive)
                consecutive = 0
        max_consecutive = max(consecutive, max_consecutive)
        return max_consecutive


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))
    print(Solution().findMaxConsecutiveOnes([1]))
    print(Solution().findMaxConsecutiveOnes([0]))

