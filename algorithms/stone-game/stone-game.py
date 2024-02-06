"""
title : 877. Stone Game
source : https://leetcode.cn/problems/stone-game/
"""
from typing import List


class Solution:
    """动态规划-空间优化

    分析状态转移方程可以看到，dp[i][j] 的值只和 dp[i+1][j] 与 dp[i][j−1] 有关，
    即在计算 dp的第 i 行的值时，只需要使用到 dp 的第 i 行和第 i+1 行的值，
    因此可以使用一维数组代替二维数组
    时间复杂度： O(n*n)
    空间复杂度： O(n)
    """
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [0] * length
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0


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
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][length - 1] > 0


class Solution2:
    """脑筋急转弯

    因为石子的总数为奇数，所以 所有奇数位之和、偶数位之和一定不相等
    先手的 Alice 只要每次都选之和最大的奇数位或偶数位，确保对手只能选择另一种则必胜
    时间复杂度： O(1)
    空间复杂度： O(1)
    """
    def stoneGame(self, piles: List[int]) -> bool:
        return True


class Solution1:
    """脑筋急转弯

    如果奇数位总和大，则先手 Alice 取奇数位，确保后手 Bob 只能取到偶数位
    如果偶数位总和大，则先手 Alice 取偶数位，确保后手 Bob 只能取到奇数位
    结果 如果奇数位之和和偶数位之和不相等则先手 Alice 一定必胜
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def stoneGame(self, piles: List[int]) -> bool:
        sum_odd, sum_even = 0, 0
        for i in range(len(piles)):
            if i % 2 == 0:
                sum_odd += piles[i]
            else:
                sum_even += piles[i]
        return sum_odd != sum_even


if __name__ == "__main__":
    print(Solution().stoneGame(piles = [5,3,4,5]))
    print(Solution().stoneGame(piles = [3,7,2,3]))
    print(Solution().stoneGame(piles = [2,5,3,3]))
