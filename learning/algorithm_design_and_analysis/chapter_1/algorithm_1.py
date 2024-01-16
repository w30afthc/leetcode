"""
算法 1：求最大公约数
输入：任意两个非负整数 a、b
输出：a、b 的最大公约数
使用欧几里得算法（辗转相除法）
"""


def euclid(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


if __name__ == "__main__":
    print(euclid(6, 8))
    print(euclid(6, 0))
    print(euclid(0, 5))
    print(euclid(3, 5))
