"""
title : 2110. Number of Smooth Descent Periods of a Stock
source : https://leetcode.cn/problems/number-of-smooth-descent-periods-of-a-stock/
"""
from typing import List


class Solution:
    """动态规划

    设 dp 数组表示以每一天为结束的平滑下降阶段的数目
    dp[i] 表示第 i 天为结尾时的平滑下降数目
    动态规划方程为： 当 i=0 时，dp[0] = 1
    当 i>1 ,且 prices[i]≠prices[i-1]-1时，dp[i]=1
    当 i>1 ,且 prices[i]=prices[i-1]-1时，dp[i]=dp[i-1]+1
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i - 1] - 1 == prices[i]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)


class Solution2:
    """双指针

    慢指针指向平滑下降阶段的开始，快指针试探平滑下降阶段的结尾
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = len(prices)
        slow = 0
        for fast in range(1, len(prices)):
            if prices[slow] - prices[fast] == fast - slow:
                ans += fast - slow
            else:
                slow = fast
        return ans


class Solution1:
    """分组循环

    外循环控制条件开始位置，内循环控制条件结束位置
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        i, n = 0, len(prices)
        while i < n:
            start = i
            i += 1
            count = 1
            while i < n and prices[i - 1] - 1 == prices[i]:
                count += 1 + i - start
                i += 1
            ans += count
        return ans


if __name__ == "__main__":
    print(Solution().getDescentPeriods(prices=[3,2,1,4]))
    print(Solution().getDescentPeriods(prices=[8,6,7,7]))
    print(Solution().getDescentPeriods(prices=[1]))
