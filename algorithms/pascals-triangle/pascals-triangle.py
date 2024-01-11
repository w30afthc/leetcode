"""
title : 118. Pascal's Triangle
source : https://leetcode.cn/problems/pascals-triangle/
"""
from typing import List


class Solution:
    """头尾补零，错位相加

    除首行外， 每行均为上一行头尾分别补零后相加而得
    时间复杂度： O(n*n)
    空间复杂度： O(1)，不考虑返回值的空间占用
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        while len(res) < numRows:
            res.append([a + b for a, b in zip([0] + res[-1], res[-1] + [0])])
        return res


class Solution4:
    """动态规划

    头尾为 1， 中间的数值为左上右上相加
    时间复杂度： O(n*n)
    空间复杂度： O(1)，不考虑返回值的空间占用
    """
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp


class Solution3:
    """暴力遍历 + 折半追加

    行首尾 1， 中间的数值为左上+右上，每行左右对称，只需要计算一半的值即可
    时间复杂度： O(n*n)
    空间复杂度： O(n)，不考虑返回值的空间占用
    """
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range((i + 2) // 2):
                if j == 0:
                    row.append(1)
                else:
                    row.append(result[i - 1][j - 1]+result[i - 1][j])
            row.extend(row[:(i+1)//2][::-1])
            result.append(row)
        return result


class Solution2:
    """暴力遍历2

    除首行外，每个数值均为其左上+右上（如果没有则为0）之和
    时间复杂度： O(n*n)
    空间复杂度： O(1)，不考虑返回值的空间占用
    """
    def generate(self, numRows: int) -> List[List[int]]:
        triangle_list = []
        for i in range(numRows):
            triangle_list.append([0]*(i+1))
            for j in range(i+1):
                if i == 0:
                    triangle_list[i][j] = 1
                elif 0 < j < i:
                    triangle_list[i][j] = triangle_list[i - 1][j-1] + triangle_list[i - 1][j]
                elif j == 0:
                    triangle_list[i][j] = 0 + triangle_list[i - 1][j]
                elif j == i:
                    triangle_list[i][j] = triangle_list[i - 1][j - 1] + 0

        return  triangle_list


class Solution1:
    """暴力遍历

    头尾为 1， 中间的数值为左上右上相加
    时间复杂度： O(n*n)
    空间复杂度： O(1)，不考虑返回值的空间占用
    """
    def generate(self, numRows: int) -> List[List[int]]:
        triangle_list = []
        for i in range(numRows):
            triangle_list.append([0]*(i+1))
            triangle_list[i][0] = triangle_list[i][-1] = 1
            for j in range(1, i):
                triangle_list[i][j] = triangle_list[i-1][j-1] + triangle_list[i-1][j]

        return triangle_list


if __name__ == "__main__":
    print(Solution().generate(5))
    print(Solution().generate(1))
    print(Solution().generate(10))
