"""
title : 94. Binary Tree Inorder Traversal
source : https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None
    root = TreeNode(nums[index])
    root.left = create_binary_tree(nums, 2 * index + 1)
    root.right = create_binary_tree(nums, 2 * index + 2)
    return root


class Solution4:
    """标记法

    用栈存储尚未遍历的数据
    栈顶数据出栈后，判断数据类型，TreeNode 类型的将其子节点和数据入继续入栈
    int 类型的添加到结果列表中， None 类型的跳过
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [root], []
        while stack:
            element = stack.pop()
            if isinstance(element, TreeNode):
                stack.extend([element.right, element.val, element.left])
            elif isinstance(element, int):
                result.append(element)
        return result


class Solution:
    """莫里斯遍历

    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                tmp = root
                root = root.left
                tmp.left = None
            else:
                ans.append(root.val)
                root = root.right
        return ans


class Solution2:
    """迭代

    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ans.append(node.val)
                root = node.right
        return ans


class Solution1:
    """递归

    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root, ans):
        if root is None:
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)


if __name__ == "__main__":
    root = [1, None, 2, None, None, 3]
    root = create_binary_tree(root, 0)
    print(Solution().inorderTraversal(root))

    root = []
    root = create_binary_tree(root, 0)
    print(Solution().inorderTraversal(root))

    root = [1]
    root = create_binary_tree(root, 0)
    print(Solution().inorderTraversal(root))
