"""
title : 209. Minimum Size Subarray Sum
source : https://leetcode.cn/problems/minimum-size-subarray-sum/description/
"""
from typing import List


class Solution:
    """前缀和 + 二分查找"""
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
    """双指针 滑动窗口2"""
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
    """双指针 滑动窗口"""
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
    """暴力遍历， 时间复杂度O(n*n)，超时了"""
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
