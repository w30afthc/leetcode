"""
title : 2. Add Two Numbers
source : https://leetcode.cn/problems/add-two-numbers/
"""
from typing import List, Optional


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
        print(elements)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    """递归

    从头到尾（从地位到高位）递归遍历链表
    时间复杂度： O(n), n 为 l1 和 l2 中最长链表长度
    空间复杂度： O(n)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        carry += l1.val + (l2.val if l2 else 0)
        l1.val = carry % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry // 10)
        return l1


class Solution:
    """模拟

    新建一个链表 l3, l3 的每个节点值等于 l1 和 l2 对应位数节点值之和（如果存在的话）
    同时需要考虑进位的问题，sum_val % 10 表示当前位的值， sum // 10 表示进位
    时间复杂度： O(n), n 为 l1 和 l2 中最长链表长度
    空间复杂度： O(n)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l3_head = l3
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            node = ListNode(carry % 10)
            carry = carry // 10
            l3.next = node
            l3 = l3.next
        return l3_head.next


if __name__ == "__main__":
    l1, l2, l3 = SinglyLinkedList(), SinglyLinkedList(), SinglyLinkedList()
    for element in [2,4,3]:
        l1.append(element)
    for element in [5,6,4]:
        l2.append(element)
    l3.head = Solution().addTwoNumbers(l1.head, l2.head)
    l3.display()

    l1, l2, l3 = SinglyLinkedList(), SinglyLinkedList(), SinglyLinkedList()
    for element in [0]:
        l1.append(element)
    for element in [0]:
        l2.append(element)
    l3.head = Solution().addTwoNumbers(l1.head, l2.head)
    l3.display()

    l1, l2, l3 = SinglyLinkedList(), SinglyLinkedList(), SinglyLinkedList()
    for element in [9,9,9,9,9,9,9]:
        l1.append(element)
    for element in [9,9,9,9]:
        l2.append(element)
    l3.head = Solution().addTwoNumbers(l1.head, l2.head)
    l3.display()
