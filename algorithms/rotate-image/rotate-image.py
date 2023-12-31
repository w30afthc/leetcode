"""
source : https://leetcode.cn/problems/rotate-image/description/
"""
from typing import List


class Solution:
    """
    先上下翻转，再按照左上到右下的对角线翻转，实现顺时针90度翻转
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution4:
    """
    以矩阵中心为界，将矩阵分为左上、右上、右下、左下四个小矩阵进行旋转
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = \
                    matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]


class Solution3:
    """
    从外到内一圈一圈的旋转
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = temp


class Solution2:
    """
    使用一个矩阵来辅助翻转，顺时针翻转即为 [i,j] <= [n-j-1,i]
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        answer = []
        for i in range(n):
            answer.append([])
            for j in range(n):
                answer[i].append(matrix[n-j-1][i])
        matrix[:] = answer


class Solution1:
    """
    使用一个矩阵来辅助翻转，顺时针翻转即为 [i,j] => [j][n-i-1]
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # matrix_new = [[0 for i in range(n)] for j in range(n)]
        matrix_new = [[None] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_new


if __name__ == "__main__":
    matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix_1)
    print(matrix_1)

    matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(matrix_2)
    print(matrix_2)

