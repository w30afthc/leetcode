"""
算法 2：在数组中查找元素
输入：元素 e 和 必然存在元素 e 且仅出现一次数组 A
输出：元素 e 在数组 A 中的下标
"""


def sequential_search(A: list, e):
    for i in range(len(A)):
        if A[i] == e:
            return i


if __name__ == "__main__":
    print(sequential_search([1, 2, 3], 2))
