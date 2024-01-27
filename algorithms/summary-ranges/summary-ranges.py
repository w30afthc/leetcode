"""
title : 228. Summary Ranges
source : https://leetcode.cn/problems/summary-ranges/
"""
from typing import List


class Solution2:
    """双指针

    思路说明
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] - nums[slow] == fast - slow:
                continue
            if fast - 1 == slow:
                ans.append("{}".format(nums[slow]))
            else:
                ans.append("{}->{}".format(nums[slow], nums[fast - 1]))
            slow = fast
        if fast == slow:
            ans.append("{}".format(nums[slow]))
        else:
            ans.append("{}->{}".format(nums[slow], nums[fast]))
        return ans


class Solution:
    """分组循环

    思路说明
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i, n = 0, len(nums)
        while i < n:
            start = i
            i += 1
            while i < n and nums[i - 1] + 1 == nums[i]:
                i += 1
            if i - 1 == start:
                ans.append("{}".format(nums[start]))
            else:
                ans.append("{}->{}".format(nums[start], nums[i - 1]))
        return ans


if __name__ == "__main__":
    print(Solution().summaryRanges(nums=[0,1,2,4,5,7]))
    print(Solution().summaryRanges(nums=[0,2,3,4,6,8,9]))
    print(Solution().summaryRanges(nums=[]))
