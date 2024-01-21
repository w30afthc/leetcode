"""
title : 705. Design HashSet
source : https://leetcode.cn/problems/design-hashset/
"""
from typing import List


class MyHashSet:
    """不定长拉链数组

    分桶取质数，确保数据能均匀的分散在各个桶中
    时间复杂度： O(n/b), n 是元素个数，b 是桶数
    空间复杂度： O(n)
    """

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key: int):
        return key % self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        return key in self.table[hashkey]


class MyHashSet2:
    """超大数组

    用数组中 key 对应位置的值来表示是否存在 key
    时间复杂度： O(1)
    空间复杂度： O(n)
    """
    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False

    def contains(self, key: int) -> bool:
        return self.set[key]


class MyHashSet1:
    """套用Python集合的概念

    不符合题意
    时间复杂度： O(1)
    空间复杂度： O(1)
    """
    def __init__(self):
        self.my_hash_set = set()

    def add(self, key: int) -> None:
        self.my_hash_set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.my_hash_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.my_hash_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
if __name__ == "__main__":
    method = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    params = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    for i in range(len(method)):
        if i == 0:
            obj = getattr(__import__("__main__"), method[0])()
            print(obj)
        else:
            print(getattr(obj, method[i])(params[i][0]))
