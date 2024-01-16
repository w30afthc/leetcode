"""
习题 1.1：3个数排序
输入：3个不同的整数
输出：3个整数排序
"""


def order(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        temp = b
        b = c
        c = temp
    return a, b, c


if __name__ == "__main__":
    print(order(2,3,1))
    print(order(3,2,1))
    print(order(1,3,2))