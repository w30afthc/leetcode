"""
title : 83. Remove Duplicates from Sorted List
source : https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
"""
from typing import List, Optional


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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """常规遍历

    遍历链表，如果当前节点和下个节点的值相等，则跳过下个节点
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


class Solution1:
    """双指针

    如果前后两个指针值相等，则移除后面的
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        while fast.next:
            fast = fast.next
            if slow.val < fast.val:
                slow = slow.next
            else:
                slow.next = fast.next
        return head


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    for element in [1, 1, 2]:
        singly_linked_list.append(element)
    singly_linked_list.head = Solution().deleteDuplicates(singly_linked_list.head)
    print(singly_linked_list.display())

    singly_linked_list = SinglyLinkedList()
    for element in [1, 1, 2, 3, 3]:
        singly_linked_list.append(element)
    singly_linked_list.head = Solution().deleteDuplicates(singly_linked_list.head)
    print(singly_linked_list.display())

    singly_linked_list = SinglyLinkedList()
    singly_linked_list.head = Solution().deleteDuplicates(singly_linked_list.head)
    print(singly_linked_list.display())
