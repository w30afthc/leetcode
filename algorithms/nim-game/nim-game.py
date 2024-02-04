"""
title : 292. Nim Game
source : https://leetcode.cn/problems/nim-game/
"""
from typing import List


class Solution2:
    """动态规划

    设状态 dp[i] 表示剩余 i+1 个石头时，先手必胜与否
    则有 dp[0] = dp[1] = dp[2] = True
    剩余 k 个石头时的先手胜负取决于后手 k-1, k-2, k-3 的胜负情况
    如果后手 k-1, k-2, k-3 三者均胜，则 k 时先手必败
    反之，如果后手 k-1, k-2, k-3 有一个必败，则 k 时先手必胜（每一步都是最优解）
    故状态状态转移方程为：dp[n] = not (dp[n-1] and dp[n-2] and dp[n-3])
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def canWinNim(self, n: int) -> bool:
        dp = [True] * 4
        for i in range(3, n):
            temp = i % 4
            dp[temp] = not (dp[temp - 1] and dp[temp - 2] and dp[temp - 3])
        return dp[(n-1) % 4]


class Solution:
    """脑筋急转弯

    如果给定的石头数量是 4, 8, 12, 16... 那么先手必输
    时间复杂度： O(1)
    空间复杂度： O(1)
    """
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


if __name__ == "__main__":
    print(Solution().canWinNim(n = 4))
    print(Solution().canWinNim(n = 1))
    print(Solution().canWinNim(n = 2))
    print(Solution().canWinNim(n = 6))
