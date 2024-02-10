"""
title : 486. Predict the Winner
source : https://leetcode.cn/problems/predict-the-winner
"""
from typing import List


class Solution1:
    """递归

    当前选法获得的分数减去后续对手获得的分数
    时间复杂度： O(2 * n), n 为数组长度
    空间复杂度： O(n)
    """
    def predictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int) -> int:
            if start == end:
                return nums[start]
            score_start = nums[start] - total(start+1, end)
            score_end = nums[end] - total(start, end-1)
            return max(score_start, score_end)

        return total(0, len(nums)-1) >= 0


class Solution2:
    """记忆化递归

    在递归的基础上记录相同状态下的分数差值
    时间复杂度： O(2 * n), n 为数组长度
    空间复杂度： O(n)
    """
    def predictTheWinner(self, nums: List[int]) -> bool:
        def total(start: int, end: int) -> int:
            if start == end:
                return nums[start]
            if memo[start][end] is not None:
                return memo[start][end]

            score_start = nums[start] - total(start+1, end)
            score_end = nums[end] - total(start, end-1)
            return max(score_start, score_end)

        length = len(nums)
        memo = [[None] * length for _ in range(length)]
        return total(0, length - 1) >= 0


class Solution3:
    """动态规划

    设二维数组 dp[i][j] 表示当剩下的石子堆为下标 i 到下标 j 时，即在下标范围 [i,j]中，
    当前玩家与另一个玩家的石子数量之差的最大值，注意当前玩家不一定是先手的 Alice
    当 i < j 时，石子堆不存在，此时 dp[i][j] = 0
    当 i = j 时，只剩下一个石子堆，当前玩家只能取走这堆石子，此时 dp[i][i] = piles[i]
    当 i < j 时，当前玩家可以取走开头的 piles[i] 或结尾的 piles[j]，让后轮到下一个玩家在剩下的石子堆中取走石子。
    在这两种方案种，当前玩家会选择最优的方案，因此状态转移方程为：
    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
    时间复杂度： O(n*n)
    空间复杂度： O(n*n)
    """
    def predictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]

        for i in range(length - 2, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])

        return dp[0][length-1] >= 0


class Solution:
    """动态规划-空间优化

    分析状态转移方程可以看到，dp[i][j] 的值只和 dp[i+1][j] 与 dp[i][j−1] 有关
    即在计算 dp 的第 i 行的值时，只需要使用到 dp 的第 i 行和第 i+1 行的值
    因此可以使用一维数组代替二维数组，对空间进行优化
    时间复杂度： O(n*n)
    空间复杂度： O(n)
    """
    def predictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [0] * length
        for i in range(length):
            dp[i] = nums[i]

        for i in range(length - 2, -1, -1):
            for j in range(i+1, length):
                dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])

        return dp[length-1] >= 0


if __name__ == "__main__":
    print(Solution().predictTheWinner(nums = [1,5,2]))
    print(Solution().predictTheWinner(nums = [1,5,233,7]))
    print(Solution().predictTheWinner(nums = [1]))
