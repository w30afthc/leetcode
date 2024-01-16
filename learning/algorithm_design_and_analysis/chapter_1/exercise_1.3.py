"""
习题1.3：集合覆盖问题
输入：给定全集 U、集合族 S
输出：最小覆盖
"""
import itertools


def mine_set_cover(U: set, S: list):
    T = []
    element_needed = U
    while element_needed:
        best_set = set()
        for Si in S:
            covered_set = element_needed & Si
            if len(covered_set) > len(best_set):
                best_set = covered_set
        element_needed -= best_set
        T.append(best_set)
    return T


if __name__ == "__main__":
    print(mine_set_cover({1,2,3,4,5}, [{1,3,5}, {2,4},{1,4},{2,5}]))
    print(mine_set_cover({1,2,3,4,5}, [{1,2,3}, {4,5},{1,2,4},{1,2,5}]))
    print(mine_set_cover({1,2,3,4,5}, [{1,2},{3},{4,5},{1,2,4},{1,2,5}]))
