"""
title : 面试题 01.08. Zero Matrix LCCI
source : https://leetcode.cn/leetbook/read/array-and-string/ciekh/
source : https://leetcode.cn/problems/zero-matrix-lcci/
"""
from typing import List


class Solution:
    """使用一个标记变量

    定义一个标志首列是否含有 0 的布尔变量，首行首列依然作为标志位；
    然后遍历整个矩阵，首列有 0 则修改标记，非首列有 0 则修改对应行首和列首；
    从右下角开始倒叙遍历整个矩阵，非首列元素依照对应的首行首列标志做清零操作，
    首列元素依照首列标志做清零
    时间复杂度： O(m*n)
    空间复杂度： O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        bool_first_col_have_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                bool_first_col_have_zero = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j == 0 and bool_first_col_have_zero:
                    matrix[i][0] = 0
                if j != 0 and (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0


class Solution3:
    """使用两个标记变量

    定义两个标志首行首列是否含有 0 的布尔变量，
    然后首行首列作为非首行首列元素是否为 0 的标志
    时间复杂度： O(m*n)
    空间复杂度： O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0


class Solution2:
    """使用标记集合

    遍历矩阵，收集有 0 的行列，最后清零
    时间复杂度： O(m*n)
    空间复杂度： O(m*n)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_row = set()
        zero_column = set()
        matrix_dic = {}

        for i in range(m):
            for j in range(n):
                matrix_dic[(i,j)] = matrix[i][j]
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_column.add(j)
        for key in matrix_dic.keys():
            if key[0] in zero_row or key[1] in zero_column:
                matrix_dic[key] = 0
        for k, v in matrix_dic.items():
            matrix[k[0]][k[1]] = v


class Solution1:
    """暴力遍历

    先找出有 0 的元素所在行列，收集所有需要清零的行列
    最后遍历整个矩阵清零
    时间复杂度： O(m*n)
    空间复杂度： O(m+n)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_column = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_column.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_row or j in zero_column:
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix_1 = [[1,1,1], [1,0,1], [1,1,1]]
    Solution().setZeroes(matrix_1)
    print(matrix_1)

    matrix_2 = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    Solution().setZeroes(matrix_2)
    print(matrix_2)
