"""
title : 1578. Minimum Time to Make Rope Colorful
source : https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/
"""
from typing import List


class Solution:
    """分组循环

    思路说明
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, n = 0, len(colors)
        cost = 0
        while i < n:
            start = i
            max_need_time = neededTime[start]
            i += 1
            while i < n and colors[start] == colors[i]:
                cost += min(max_need_time, neededTime[i])
                if neededTime[i] > max_need_time:
                    max_need_time = neededTime[i]
                i += 1
        return cost


if __name__ == "__main__":
    print(Solution().minCost(colors = "abaac", neededTime = [1,2,3,4,5]))
    print(Solution().minCost(colors = "abc", neededTime = [1,2,3]))
    print(Solution().minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))
