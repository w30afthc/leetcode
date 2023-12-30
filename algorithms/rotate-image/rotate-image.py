"""
source : https://leetcode.cn/problems/rotate-image/description/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        pass


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
        return answer


class Solution1:
    """
    使用一个矩阵来辅助翻转，顺时针翻转即为 [i,j] => [j][n-i-1]
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix2 = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix2[j][n-i-1] = matrix[i][j]
        return matrix2


if __name__ == "__main__":
    print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

