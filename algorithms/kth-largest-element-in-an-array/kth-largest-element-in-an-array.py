"""
title : 215. Kth Largest Element in an Array
source : https://leetcode.cn/leetbook/read/sort-algorithms/osxtdc/
source : https://leetcode.cn/problems/kth-largest-element-in-an-array/
"""
from typing import List


class Solution:
    """堆排序

    时间复杂度： O(n*log n)
    空间复杂度： O(1)
    """
    def maxHeapify(self, arr, i, end):
        j = 2 * i + 1
        while j <= end:
            if j + 1 <= end and arr[j+1] > arr[j]:
                j += 1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
                j = 2 * i + 1
            else:
                break

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n//2-1, -1, -1):
            self.maxHeapify(nums, i, n-1)

        for j in range(n-1, n-k-1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.maxHeapify(nums, 0, j-1)

        return nums[-k]


class Solution2:
    """快速排序 + 分治

    分治后得出分治位置在数组排序后中的位置，从分治位置向位置 k 递归逼近
    时间复杂度： O(n*log n)
    空间复杂度： O(log n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            partition_index = self.partition(nums, left, right)
            if partition_index > k - 1:
                right = partition_index - 1
            elif partition_index < k - 1:
                left = partition_index + 1
            else:
                return nums[partition_index]

    def partition(self, array, left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if array[pivot] < array[i]:
                array[i], array[index] = array[index], array[i]
                index += 1
            i += 1
        array[pivot], array[index-1] = array[index-1], array[pivot]
        return index - 1


class Solution1:
    """选择排序

    选出最大的元素，放在最前面
    再从剩下的元素中选择次最大的元素，放在第二个位置
    重复上述过程直至第 k 个最大的元素
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            max_index = i
            for j in range(i + 1, len(nums)):
                if nums[max_index] < nums[j]:
                    max_index = j
            nums[i], nums[max_index] = nums[max_index], nums[i]

        return nums[i]


if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], k=2))
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k=4))
    print(Solution().findKthLargest([1,2,3],2))
    print(Solution().findKthLargest([1,2,3,1,2,3,3,2,1],2))
