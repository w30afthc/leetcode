"""
title : 912. Sort an Array
source : https://leetcode.cn/leetbook/read/sort-algorithms/eunjmt/
source : https://leetcode.cn/problems/sort-an-array/
"""
from typing import List


class Solution:
    """快速排序"""
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left < right:
            partition_index = self.partition(nums, left, right)
            self.quick_sort(nums, left, partition_index - 1)
            self.quick_sort(nums, partition_index + 1, right)

    def partition(self, nums, left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if nums[pivot] > nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
            i += 1
        nums[pivot], nums[index - 1] = nums[index - 1], nums[pivot]
        return index - 1


class Solution1:
    """插入排序

    维护前面的元素为已排序序列（初始为 1 个元素）
    每次从后面未排序的序列取一个元素 current
    如果 current 小于前面已排序序列的末尾，则 current 应插在前面
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            current = nums[i]
            pre_index = i - 1
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index + 1] = nums[pre_index]
                pre_index -= 1
            nums[pre_index + 1] = current
        return nums


if __name__ == "__main__":
    print(Solution().sortArray([5,2,3,1]))
    print(Solution().sortArray([5,1,1,2,0,0]))
    print(Solution().sortArray([-1,-2,0,3]))
