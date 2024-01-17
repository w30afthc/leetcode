"""
title : 561. Array Partition
source : https://leetcode.cn/leetbook/read/array-and-string/c24he/
source : https://leetcode.cn/problems/array-partition/
"""
from typing import List


class Solution:
    """排序后取切片

    排序后取切片求和
    时间复杂度： O(n*log n)，即为对数组 nums 进行排序的时间复杂度
    空间复杂度： O(log n)，即为排序需要使用的栈空间
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


class Solution1:
    """排序后取最小值求和

    将数组排序后，挨个两两组合，其最小值的总和即为最大和
    时间复杂度： O(n*log n)，即为对数组 nums 进行排序的时间复杂度
    空间复杂度： O(log n)，即为排序需要使用的栈空间
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, max_sum = 0, 0
        while i < len(nums):
            max_sum += min(nums[i], nums[i+1])
            i += 2
        return max_sum


if __name__ == "__main__":
    print(Solution().arrayPairSum([1,4,3,2]))
    print(Solution().arrayPairSum([6,2,6,5,1,2]))
    print(Solution().arrayPairSum([10,2,4,3,5,6,7,8,9,1]))
