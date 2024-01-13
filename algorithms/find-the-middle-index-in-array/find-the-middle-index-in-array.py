"""
title : 1991. Find the Middle Index in Array
source : https://leetcode.cn/leetbook/read/array-and-string/yf47s/
source : https://leetcode.cn/problems/find-the-middle-index-in-array/
source : https://leetcode.cn/problems/find-pivot-index
"""
from typing import List


class Solution:
    """常规解法

    计算出数组总和，依次遍历数组计算出左边和
    如果 2 倍左边和 + 当前位置数 = 总和，则满足条件
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            if left_sum*2 + num == total:
                return i
            left_sum += num
        return -1


class Solution2:
    """
    常规解法

    计算出数组总和，依次遍历数组计算出左边和
    如果 2 倍左边和 + 当前位置数 = 总和，则满足条件
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i in range(len(nums)):
            if left_sum*2 + nums[i] == total:
                return i
            left_sum += nums[i]
        return -1


class Solution1:
    """常规解法

    计算出数组总和（即为初始右边和），依次遍历数组计算出左边和、右边（+-当前位置数）
    对比左边和与右边和，得出结论
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
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
