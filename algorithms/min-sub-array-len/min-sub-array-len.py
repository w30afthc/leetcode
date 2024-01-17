"""
title : 209. Minimum Size Subarray Sum
source : https://leetcode.cn/leetbook/read/array-and-string/c0w4r/
source : https://leetcode.cn/problems/minimum-size-subarray-sum/
"""
from typing import List


class Solution:
    """前缀和 + 二分查找

    构建原数组的前缀和数组，表示原数组每个位置的前缀累加之和
    在前缀和中二分查找大于等于目标值的位置
    时间复杂度： O(n* log n)
    空间复杂度： O(n)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        total, ans = 0, n + 1
        # sums = [sum(nums[0:i]) for i in range(n)]
        sums = [nums[0]]
        for i in range(1, n):
            sums.append(sums[i-1] + nums[i])

        for i in range(n):
            left, right = i, n - 1
            while left <= right:
                mid = (left + right) // 2
                if sums[mid] - sums[i] + nums[i] >= target:
                    ans = min(ans, mid - i + 1)
                    right = mid - 1
                else:
                    left = mid + 1

        return 0 if ans == n + 1 else ans


class Solution3:
    """双指针 滑动窗口2

    快慢指针指向数组开始，总和 = 从 0 开始到快指针的累加 - 从 0 开始到慢指针的累加
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums_length = len(nums)
        i, sum_subarray, minima_length = 0, 0, nums_length + 1
        for j in range(nums_length):
            sum_subarray += nums[j]
            while sum_subarray >= target:
                minima_length = min(minima_length, j-i+1)
                sum_subarray -= nums[i]
                i += 1
        return minima_length if minima_length <= nums_length else 0


class Solution2:
    """双指针 滑动窗口

    快慢指针指向数组开始，总和 = 从 0 开始到快指针的累加 - 从 0 开始到慢指针的累加
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        fast, slow, total = 0, 0, 0
        while fast < len(nums) and slow < len(nums):
            total += nums[fast]
            if total < target:
                fast += 1
            else:
                ans = min(fast - slow + 1, ans)
                total = total - nums[slow] - nums[fast]
                slow += 1

        if ans < len(nums) + 1:
            return ans
        else:
            return 0


class Solution1:
    """暴力遍历

    遍历数组中的每一个位置，依次以该位置为起点向后依次累加
    找到大于等于目标值的长度，找出最小长度
    时间复杂度： O(n*n)，超时了
    空间复杂度： O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    ans = min(ans, j-i+1)
                    break
            if total < target:
                break
        return ans if ans <= n else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
    print(Solution().minSubArrayLen(4, [1,4,4]))
    print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    print(Solution().minSubArrayLen(3, [4]))
    print(Solution().minSubArrayLen(4, [4]))
    print(Solution().minSubArrayLen(5, [4]))
    print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
