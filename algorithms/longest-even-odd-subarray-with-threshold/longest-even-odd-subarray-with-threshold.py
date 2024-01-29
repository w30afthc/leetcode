"""
title : 2760. Longest Even Odd Subarray With Threshold
source : https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/
"""
from typing import List


class Solution:
    """动态规划-空间优化

    设状态 dp 表示到 i 为止的奇偶子数组长度
    则有 当 nums[i] > threshold 时， dp = 0
    如果 dp 不为 0，则当前数值属于奇偶子数组，判断下一个数值是否满足前面的奇偶间隔规律
    如果满足则 dp = dp + 1，如果不满足则判断当前数值是否是偶数
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        dp, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] <= threshold:
                if dp > 0 and nums[i] % 2 == dp % 2:
                    dp = dp + 1
                elif nums[i] % 2 == 0:
                    dp = 1
                else:
                    dp = 0
            else:
                dp = 0
            ans = max(ans, dp)
        return ans


class Solution4:
    """动态规划

    设状态数组 dp[i] 表示到 i 为止的奇偶子数组长度
    则有 当 nums[i] > threshold 时， dp[i] = 0
    如果 dp[i-1] 不为 0，则前面的子数组是奇偶子数组，判断当前数值是否满足前面的奇偶间隔规律
    如果满足则 dp[i] = dp[i-1] + 1，如果不满足则判断当前数值是否是偶数
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if nums[i] <= threshold:
                if dp[i-1] > 0 and nums[i] % 2 == dp[i-1] % 2:
                    dp[i] = dp[i-1] + 1
                elif nums[i] % 2 == 0:
                    dp[i] = 1
        return max(dp)


class Solution3:
    """双指针

    左指针 l 记录最长奇偶子数组开始位置，右指针 r 试探结束位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        l = 0
        for r in range(len(nums)):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                if nums[r] <= threshold and nums[r] % 2 == (r - l) % 2:
                    pass
                else:
                    l = r
                ans = max(ans, r - l + 1)
            else:
                l += 1
        return ans


class Solution2:
    """分组循环

    外层循环负责记录奇偶子数组开始位置和更新最大长度
    内层循环负责遍历奇偶子数组，找出结束位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            start = i
            i += 1
            if nums[start] % 2 == 1 or nums[start] > threshold:
                continue
            while i < n and nums[i - 1] % 2 != nums[i] % 2 and nums[i] <= threshold:
                i += 1
            ans = max(ans, i - start)

        return ans


class Solution1:
    """暴力遍历

    外层循环寻找奇偶子数组开始位置
    内层循环负责遍历奇偶子数组，找出结束位置
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            if nums[i] > threshold or nums[i] % 2 == 1:
                continue
            for j in range(i, n):
                if nums[j] <= threshold and nums[j] % 2 == (j - i) % 2:
                    ans = max(ans, j - i + 1)
                else:
                    break
        return ans


if __name__ == "__main__":
    print(Solution().longestAlternatingSubarray(nums=[3,2,5,4], threshold=5))
    print(Solution().longestAlternatingSubarray(nums=[2,3,4,5], threshold=4))
    print(Solution().longestAlternatingSubarray(nums=[2,2,1], threshold=4))
    print(Solution().longestAlternatingSubarray(nums=[4], threshold=4))
    print(Solution().longestAlternatingSubarray(nums=[5], threshold=4))
    print(Solution().longestAlternatingSubarray(nums=[1,2], threshold=2))
    print(Solution().longestAlternatingSubarray(nums=[10,4,10,8,7,8], threshold=8))
