"""
title : 1578. Minimum Time to Make Rope Colorful
source : https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/
"""
from typing import List


class Solution:
    """双指针

    慢指针指向连续相同颜色气球的开始，快指针试探连续相同颜色气球的结束
    快指针记录相同颜色气球移除耗时最高的，cost 累加其余耗时
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        slow, cost = 0, 0
        max_needed_time = neededTime[slow]
        for fast in range(1, len(colors)):
            if colors[slow] == colors[fast]:
                cost += min(max_needed_time, neededTime[fast])
                if neededTime[fast] > max_needed_time:
                    max_needed_time = neededTime[fast]
            else:
                slow = fast
                max_needed_time = neededTime[slow]
        return cost


class Solution1:
    """分组循环

    找出连续的相同颜色的气球，统计其中较小的时间
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
    print(Solution().minCost(colors="abaac", neededTime=[1,2,3,4,5]))
    print(Solution().minCost(colors="abc", neededTime=[1,2,3]))
    print(Solution().minCost(colors="aabaa", neededTime =[1,2,3,4,1]))
