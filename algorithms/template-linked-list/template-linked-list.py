"""
title : number.Title Name
source : https://leetcode.cn/problems/***/description/
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
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
    """解法名称

    思路说明
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def funcitonName(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    for element in [4,2,1,3]:
        singly_linked_list.append(element)
    print(singly_linked_list.display())
    singly_linked_list.head = Solution().funcitonName(singly_linked_list.head)
    print(singly_linked_list.display())
