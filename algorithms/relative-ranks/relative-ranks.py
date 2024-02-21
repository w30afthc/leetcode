"""
title : 506. Relative Ranks
source : https://leetcode.cn/leetbook/read/sort-algorithms/et905c/
source : https://leetcode.cn/problems/relative-ranks/
"""
from typing import List


class Solution:
    """希尔排序

    排序后，依次找出数组中每个元素的排名
    时间复杂度： O(n * n)
    空间复杂度： O(n)
    """
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_score = score[:]
        length = len(sort_score)
        gap = length // 2
        while gap > 0:
            for i in range(gap, length):
                current = sort_score[i]
                pre_index = i - gap
                while pre_index >= 0 and sort_score[pre_index] < current:
                    sort_score[pre_index + gap] = sort_score[pre_index]
                    pre_index -= gap
                sort_score[pre_index + gap] = current
            gap //= 2

        answer = []
        for a in score:
            if sort_score.index(a) == 0:
                answer.append("Gold Medal")
            elif sort_score.index(a) == 1:
                answer.append("Silver Medal")
            elif sort_score.index(a) == 2:
                answer.append("Bronze Medal")
            else:
                answer.append(str(sort_score.index(a)+1))

        return answer


if __name__ == "__main__":
    print(Solution().findRelativeRanks(score = [5,4,3,2,1]))
    print(Solution().findRelativeRanks(score = [10,3,8,9,4]))
    print(Solution().findRelativeRanks(score = [10]))
