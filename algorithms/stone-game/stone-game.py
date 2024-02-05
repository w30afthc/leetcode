"""
title : 877. Stone Game
source : https://leetcode.cn/problems/stone-game/
"""
from typing import List


class Solution:
    """动态规划


    时间复杂度： O(1)
    空间复杂度： O(1)
    """
    def stoneGame(self, piles: List[int]) -> bool:
        pass


class Solution2:
    """脑筋急转弯

    因为石子的总数为奇数，所以 所有奇数位之和、偶数位之和一定不相等
    先手的 Alice 只要每次都选之和最大的奇数位或偶数，确保对手只能选择另一种则必胜
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
