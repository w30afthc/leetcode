"""
title : 2765. Longest Alternating Subarray
source : https://leetcode.cn/problems/longest-alternating-subarray/
"""
from typing import List


class Solution:
    """分组循环

    外层循环探测开始的位置，探测到后进入内层循环
    内层循环探测结束的位置，探测到后退出内层循环
    开始位置 - 结束位置 就是检测到的满足题意的交替子数组长度
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            start = i
            i += 2
            while i < n and nums[i] == nums[i - 2]:
                i += 1
            ans = max(ans, i - start)
            i -= 1
        return ans


class Solution2:
    """单循环

    如果当前元素和前一个元素差 1，则进入交替数组状态
    接下来按照交替数组定义，判断交替数组长度
    如果不满足交替数组定义则退出交替数组状态，从当前位置重新判断
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def alternatingSubarray(self, nums: List[int]) -> int:
        i, n = 1, len(nums)
        start, longest_length = 0, -1
        flag = False
        while i < n:
            if not flag and nums[i] - nums[i-1] == 1:
                start = i - 1
                flag = True

            if flag:
                if nums[i] - nums[i-1] == (-1) ** (i - start + 1):
                    longest_length = max(longest_length, i - start + 1)
                else:
                    flag = False
                    i -= 1
            i += 1

        return longest_length


class Solution1:
    """暴力模拟

    数组中每个元素作为初始元素，如果每两个元素的差值满足交易子数组定义
    则更新最长交替子数组长度
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def alternatingSubarray(self, nums: List[int]) -> int:
        longest_length = -1
        for i in range(len(nums) - 1):
            for j in range(i, len(nums) - 1):
                if nums[j+1] - nums[j] == (-1)**(j-i):
                    longest_length = max(longest_length, j - i + 2)
                else:
                    break
        return longest_length


if __name__ == "__main__":
    print(Solution().alternatingSubarray([2,3,4,3,4]))
    print(Solution().alternatingSubarray([4,5,6]))
    print(Solution().alternatingSubarray([2,3]))
    print(Solution().alternatingSubarray([2,4]))
    print(Solution().alternatingSubarray([42,43,44,43,44,43,44,45,46]))
