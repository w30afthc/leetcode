"""
title: 167. Two Sum II - Input Array Is Sorted
source : https://leetcode.cn/leetbook/read/array-and-string/cnkjg/
source : https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    """双指针 + 二分法

    间复杂度： O(n)
    空间复杂度： O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            middle = (right + left) // 2
            if numbers[left] + numbers[middle] > target:
                right = middle - 1
            if numbers[middle] + numbers[right] < target:
                left = middle + 1

            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]


class Solution3:
    """双指针

    初始左右指针分别指向数组的头尾，如果左右指针对应数之和为目标值则返回
    如果之和小于目标值，则左指针前进
    如果之和大于目标值，则右指针后退
    因为数组按非递减顺序排列，且存在唯一的答案，所以一定能找到
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            # 恰巧相等的概率最小，最后判断
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return [-1, -1]


class Solution2:
    """哈希表

    对于数组中的每个数，如果该数与目标值的差值不在哈希表中，则添加该数与对应下标哈希表中
    如果在哈希表中则返回差值对应的下标和当前数的下标
    HashTable 不满足使用常量级的额外空间要求
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, number in enumerate(numbers, 1):
            if target - number in hashtable:
                return [hashtable[target-number], i]
            else:
                hashtable[number] = i
        return [-1, -1]


class Solution1:
    """暴力遍历

    对于数组中的每个数，计算其与目标值的差值，查看该差值是否在剩下的数组中
    时间复杂度过高
    时间复杂度： O(n*n*n)
    空间复杂度： O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[i+1:]:
                return [i+1, numbers.index(target-numbers[i], i+1)+1]
        return [-1, -1]


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([2,3,4], 6))
    print(Solution().twoSum([-1,0], -1))
    print(Solution().twoSum([0,0,3,4], 0))
    print(Solution().twoSum([1,2,3,4,4,9,56,90], 8))
    print(Solution().twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997],542))
