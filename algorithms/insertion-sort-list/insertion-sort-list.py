"""
title : 147. Insertion Sort List
source : https://leetcode.cn/leetbook/read/sort-algorithms/euvypr/
source : https://leetcode.cn/problems/insertion-sort-list/
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.val)
            current = current.next
        return elements


class Solution:
    """插入排序

    记录前方已排序完成的节点的末尾 last_sorted
    用 last_sorted 的值与当前节点 current 的值对比
    如果小于等于则追加到已完成排序节点末尾（无需操作），last_sorted, current 前进即可
    如果大于则需要从头开始查找大于 current.val 的节点 previous.next，并在 previous 之后插入
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last_sorted = head
        current = head.next
        while current:
            if last_sorted.val <= current.val:
                last_sorted = last_sorted.next
            else:
                previous = dummy
                while previous.next.val <= current.val:
                    previous = previous.next
                last_sorted.next = current.next
                current.next = previous.next
                previous.next = current
            current = last_sorted.next
        return dummy.next


class Solution1:
    """常规解法

    找到当前不按顺序排列的节点，移除该节点
    将该节点重新插入到链表中
    时间复杂度： O(n*n)
    空间复杂度： O(1)
    """
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        while current.next.next:
            if current.next.val <= current.next.next.val:
                current = current.next
            else:
                val = current.next.next.val
                current.next.next = current.next.next.next
                self.singly_linked_insert(dummy, val)
        return dummy.next

    def singly_linked_insert(self, dummy, val):
        current = dummy
        while current.next:
            if current.next.val > val:
                node = ListNode(val)
                node.next = current.next
                current.next = node
                return dummy
            else:
                current = current.next
        current.next = ListNode(val)
        return dummy


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    for element in [4,2,1,3]:
        singly_linked_list.append(element)
    print("排序前", singly_linked_list.display())
    singly_linked_list.head = Solution().insertionSortList(singly_linked_list.head)
    print("排序后", singly_linked_list.display())

    singly_linked_list = SinglyLinkedList()
    for element in [-1,5,3,4,0]:
        singly_linked_list.append(element)
    print("排序前", singly_linked_list.display())
    singly_linked_list.head = Solution().insertionSortList(singly_linked_list.head)
    print("排序后", singly_linked_list.display())

    singly_linked_list = SinglyLinkedList()
    for element in [1, 2, 0]:
        singly_linked_list.append(element)
    print("排序前", singly_linked_list.display())
    singly_linked_list.head = Solution().insertionSortList(singly_linked_list.head)
    print("排序后", singly_linked_list.display())
