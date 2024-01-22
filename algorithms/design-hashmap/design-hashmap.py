"""
title : 706. Design HashMap
source : https://leetcode.cn/leetbook/read/lc-class-hash/wvpvtd/
source : https://leetcode.cn/problems/design-hashmap/
"""
from typing import List


class MyHashMap:
    """不定长拉链数组

    将哈希映射设计为 质数个分桶，确保数据能均匀的分散在各个桶中
    桶中有数据时，依次在后添加
    时间复杂度： O(n/b), n 是元素个数，b 是桶数
    空间复杂度： O(n)
    """

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key: int):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                self.table[hashkey].remove(item)
                return


class MyHashMap2:
    """定长拉链数组

    把哈希映射设计为 1000 * 1001 的二维数组
    时间复杂度： O(1)
    空间复杂度： O(n)
    """

    def __init__(self):
        self.buckets = 1000
        self.itemsPreBucket = 1001
        self.map = [[-1] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        if self.map[hashkey] == [-1]:
            self.map[hashkey] = [-1] * self.itemsPreBucket
        self.map[hashkey][self.pos(key)] = value

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        if self.map[hashkey] == [-1]:
            return -1
        return self.map[hashkey][self.pos(key)]

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if self.map[hashkey] != [-1]:
            self.map[hashkey][self.pos(key)] = -1


class MyHashMap1:
    """超大数组

    用列表中下标来表示 key ，对应位置的值来表示 value
    时间复杂度： O(1)
    空间复杂度： O(n)
    """
    def __init__(self):
        self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map[key] is None:
            return -1
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
if __name__ == "__main__":
    method = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get", "remove", "get", "put"]
    params = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2], [0], [0], [0, 0]]
    for i in range(len(method)):
        if i == 0:
            obj = getattr(__import__("__main__"), method[0])()
            print(obj)
        else:
            print(getattr(obj, method[i])(*params[i]))
