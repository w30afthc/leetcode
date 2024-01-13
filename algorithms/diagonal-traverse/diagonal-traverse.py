"""
title : 498. Diagonal Traverse
source : https://leetcode.cn/leetbook/read/array-and-string/cuxq3/
source : https://leetcode.cn/problems/diagonal-traverse/
"""
from typing import List


class Solution:
    """直接模拟

    依照对角线遍历的规则，依次给对角线数组赋值
    时间复杂度： O(m*n)
    空间复杂度： O(1)，除返回值外不需要额外的空间
    """
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diagonal_list = []  # 对角线数组
        i = j = 0
        for line in range(m+n-1):
            if line % 2:
                flag_direction = 1
            else:
                flag_direction = -1
            while i + j == line:
                diagonal_list.append(mat[i][j])
                i = i + flag_direction
                j = j - flag_direction
                if i >= m:
                    i -= 1
                    j += 2
                if j >= n:
                    j -= 1
                    i += 2
                if i < 0:
                    i += 1
                if j < 0:
                    j += 1
        return diagonal_list


if __name__ == "__main__":
    print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().findDiagonalOrder([[1,2],[3,4]]))
    print(Solution().findDiagonalOrder([[n+7*m for n in range(1,8)] for m in range(5)]))
