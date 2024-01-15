"""
title : 82. Remove Duplicates from Sorted List II
source : https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
"""
from typing import List, Optional


class SingleLinkList:
    def __init__(self):
        self.head = None

    def append(self, item):
        node = ListNode(item)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """快中慢指针

    两个指针判断是否有重复，一个指针记录删除重复之后的链表
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        count = 1
        new_head = ListNode(0)
        slow, mid, fast = new_head, head, head.next
        while fast:
            if mid.val == fast.val:
                count += 1
                slow.next = None
            else:
                if count > 1:
                    slow.next = fast
                else:
                    slow.next = mid
                    slow = slow.next
                mid = fast
                count = 1
            fast = fast.next
        return new_head.next


if __name__ == "__main__":
    single_link = SingleLinkList()
    for node in [1,2,3,3,4,4,5]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

    single_link = SingleLinkList()
    for node in [1,1,1,2,3]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

    single_link = SingleLinkList()
    for node in [1,1,2]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

    single_link = SingleLinkList()
    for node in [1, 2, 2]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()
