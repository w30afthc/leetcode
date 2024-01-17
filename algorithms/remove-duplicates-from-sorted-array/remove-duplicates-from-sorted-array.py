"""
title : 26. Remove Duplicates from Sorted Array
source : https://leetcode.cn/leetbook/read/array-and-string/cq376/
source : https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    """通用解法

    将最多 只出现一次 变为 最多只出现 m 次，参数化以解决更具有一般性的问题
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def get_most_n_element_list_length(self, nums: List[int], n: int) -> int:
        if len(nums) < 1 or n < 1:
            return 0
        pointer = 0
        for index in range(len(nums)):
            if pointer < n or nums[pointer - n] != nums[index]:
                nums[pointer] = nums[index]
                pointer += 1
        return pointer

    def removeDuplicates(self, nums: List[int]) -> int:
        return self.get_most_n_element_list_length(nums, 1)


class Solution4:
    """双指针

    快指针找不同的值，赋值给慢指针
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] < nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


class Solution3:
    """引入辅助数组

    不等的追加到新数组中
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        temp_list = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != temp_list[-1]:
                temp_list.append(nums[i])
        nums[:] = temp_list
        return len(nums)


class Solution2:
    """正常遍历

    相等的挑出来删除
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i] < nums[i + 1]:
                i += 1
            elif nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                n -= 1
            else:
                break
        return n


class Solution1:
    """正常遍历

    相等的挑出来追加到队尾
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                i += 1
            elif nums[i] == nums[i + 1]:
                nums.append(nums.pop(i + 1))
            else:
                break
        return i + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2]))
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(Solution().removeDuplicates([3]))
    print(Solution().removeDuplicates([2,3]))
