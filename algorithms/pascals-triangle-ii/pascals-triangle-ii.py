"""
title : 119. Pascal's Triangle II
source : https://leetcode.cn/problems/pascals-triangle-ii/
"""
from typing import List


class Solution:
    """线性递推

    思路说明
    时间复杂度： O(n)
    空间复杂度： O(1), 不考虑返回值的空间占用
    """
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex+1):
            ans.append(round(ans[i-1] * (rowIndex + 1 - i) / i))
        return ans


class Solution2:
    """倒叙生成

    只用一行记录最后一行的数据
    时间复杂度： O(n*n)
    空间复杂度： O(1)，不考虑返回值的空间占用
    """
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex + 1):
            for j in range(i, 0, -1):
                if j == i:
                    row.append(1)
                else:
                    row[j] = row[j - 1] + row[j]
        return row


class Solution1:
    """正常遍历

    首尾都是 1，中间的数值为上一层的左右相加
    时间复杂度： O(n*n)
    空间复杂度： O(n*n)，不考虑返回值的空间占用
    """
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(row)
        return row


if __name__ == "__main__":
    print(Solution().getRow(3))
    print(Solution().getRow(0))
    print(Solution().getRow(1))
