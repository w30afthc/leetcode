"""
title : 83. Remove Duplicates from Sorted List
source : https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
"""
from typing import List, Optional


# Definition for singly-linked list.
class SinglyLinkList:
    def __int__(self):
        self._head = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head = Solution().deleteDuplicates(head)
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head = Solution().deleteDuplicates(head)
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

    head = None
    head = Solution().deleteDuplicates(head)
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
