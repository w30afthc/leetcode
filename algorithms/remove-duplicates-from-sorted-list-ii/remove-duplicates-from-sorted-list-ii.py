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
    """利用计数，两次遍历

    第一次遍历统计每个节点的值出现的次数
    第二次遍历跳过值出现不止1次的节点
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        val_dict = {}
        while head:
            if head.val in val_dict:
                val_dict[head.val] += 1
            else:
                val_dict[head.val] = 1
            head = head.next

        head = dummy
        while head.next:
            if val_dict[head.next.val] == 1:
                head = head.next
            else:
                head.next = head.next.next
        return dummy.next


class Solution3:
    """递归

    每次只在链表前找两个不同的值的节点
    如果节点1和节点2不同，则保留节点1，递归继续判断节点2
    如果节点1和节点2相同，则记录节点1，继续向下找，直到直到一个不同值的节点，并递归继续判断这个节点
    如果当前节点为空或当前节点没有下一节点，则结束递归
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move and head.val == move.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head


class Solution2:
    """一次遍历

    头部前添加一个节点，防止原先头部节点也是重复的，当前指针从新的头部节点开始
    如果当前指针的下一个节点和下下一个节点（如果存在的话）的值相同，则记录该值
    从下一个节点开始寻找，直到找到与该值不同的节点，跳过这些值，将当前节点的下一个节点指向新的不同的值的节点
    如果当前指针的下一个节点和下下一个节点不同，则将当前节点指向它的下一节点
    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


class Solution1:
    """快中慢指针

    两个指针判断是否有重复，一个指针记录删除重复之后的链表
    时间复杂度： O(n)
    空间复杂度： O(1)
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
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

    single_link = SingleLinkList()
    for node in [1,1,1,2,3]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

    single_link = SingleLinkList()
    for node in [1,1,2]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

    single_link = SingleLinkList()
    for node in [1, 2, 2]:
        single_link.append(node)
    head = Solution().deleteDuplicates(single_link.head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()
