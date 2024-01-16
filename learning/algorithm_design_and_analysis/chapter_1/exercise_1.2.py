"""
习题 1.2：3个数的中位数
输入：3个各不相同的整数
输出：3个整数的中位数
"""


def median(a, b, c):
    if b < a < c or b > a > c:
        return a
    if a < b < c or a > b > c:
        return b
    return c


if __name__ == "__main__":
    print(median(2,3,1))
    print(median(3,2,1))
    print(median(1,3,2))