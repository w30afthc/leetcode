"""
title : 1887. Reduction Operations to Make the Array Elements Equal
source : https://leetcode.cn/problems/reduction-operations-to-make-the-array-elements-equal/
"""
from typing import List


class Solution:
    """排序后计数

    先降序排序，然后遍历数组，统计操作次数
    每当当前数值比前一个数值大时，操作次数就需要增加 1
    时间复杂度： O(n*log n)
    空间复杂度： O(log n)
    """
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count, step = 0, 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                step += 1
            count += step
        return count


class Solution2:
    """分组循环

    先降序排序，然后分组循环遍历数组（无需更改数值，只需要计数即可）
    找出每个层级拥有多少个相同的数字，这个层级的数字被操作后会减少降低到下一个层级
    最后一层无需减少，因此最后统计时扣除
    时间复杂度： O(n*log n)
    空间复杂度： O(log n)
    """
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        i, n = 0, len(nums)
        nums.sort(reverse=True)
        while i < n:
            start = i
            while i < n and nums[i] == nums[start]:
                i += 1
            ans += i
        return ans - n


class Solution1:
    """模拟

    模拟题设操作步骤，先在数组中找出第一个最大的数，然后找出小于最大数的第二大数
    如果第一大与第二大不同，则将第一大减少到第二大，操作次数 + 1
    如果第一大与第二大相同，则结束查找
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        while True:
            largest, next_largest = 0, 0
            for i in range(n):
                if nums[i] > nums[largest]:
                    largest = i
                if nums[i] < nums[next_largest]:
                    next_largest = i
            for i in range(n):
                if nums[i] != nums[largest] and nums[i] > nums[next_largest]:
                    next_largest = i
            if nums[largest] != nums[next_largest]:
                nums[largest] = nums[next_largest]
                ans += 1
            else:
                break
        return ans


if __name__ == "__main__":
    print(Solution().reductionOperations(nums = [5,1,3]))
    print(Solution().reductionOperations(nums = [1,1,1]))
    print(Solution().reductionOperations(nums = [1,1,2,2,3]))
