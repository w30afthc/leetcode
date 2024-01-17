"""
title : 485. Max Consecutive Ones
source : https://leetcode.cn/leetbook/read/array-and-string/cd71t/
source : https://leetcode.cn/problems/max-consecutive-ones/
"""
from typing import List


class Solution:
    """双指针

    慢指针指向数字1前最后一个0的位置，快指针与慢指针的差值即为连续1的个数
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, slow = 0, -1
        for fast in range(len(nums)):
            if nums[fast] == 0:
                slow = fast
            if fast - slow > ans:
                ans = fast - slow
        return ans


class Solution1:
    """通用解法

    记录连续1的个数和最大连续个数
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
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
