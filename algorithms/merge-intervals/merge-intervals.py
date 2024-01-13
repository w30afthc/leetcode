"""
title : 56. Merge Intervals
source : https://leetcode.cn/leetbook/read/array-and-string/c5tv3/
source : https://leetcode.cn/problems/merge-intervals/
"""
from typing import List


class Solution:
    """排序算法

    将数组排序，相连两个区间若头尾相交，则可以合并
    合并后取前一个区间的头，前后区间最大的尾
    时间复杂度： O(n·log n), 快递排序的时间消耗
    空间复杂度： O(log n), 返回值之外的排序所需空间
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answers = []
        intervals.sort()
        for interval in intervals:
            if not answers or answers[-1][-1] < interval[0]:
                answers.append(interval)
            else:
                answers[-1][-1] = max(answers[-1][-1], interval[1])
        return answers


class Solution1:
    """暴力计算

    遍历数组，挨个检查当前区间与已合并的区间是否有重叠
    没有则追加到已合并的数组中，有则合并，并递归
    时间复杂度： O(n*n)
    空间复杂度： O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answers = []
        for interval in intervals:
            middle = answers
            merge_flag = False
            for j in range(len(answers)):
                if interval[0] <= answers[j][1] and interval[1] >= answers[j][0]:
                    answers[j] = [min(interval[0], answers[j][0]), max(interval[1], answers[j][1])]
                    middle = self.merge(answers)
                    merge_flag = True
            if not merge_flag:
                middle.append(interval)
            answers = middle
        # 去重
        result = []
        for answer in answers:
            if answer not in result:
                result.append(answer)
        return result


if __name__ == "__main__":
    print(Solution().merge([[2,3],[4,6],[5,7],[3,4]]))
    print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
    print(Solution().merge([[2,3],[4,5],[1,10],[6,7],[8,9]]))
    print(Solution().merge([[1,10],[2,3],[4,5],[6,7],[8,9]]))
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
    print(Solution().merge([[1,4],[4,5]]))
    print(Solution().merge([[1,3],[3,3],[1,2]]))
    print(Solution().merge([[1,4],[0,4]]))
    print(Solution().merge([[3,5],[2,3]]))
    print(Solution().merge([[1,2],[4,5],[2,3]]))
