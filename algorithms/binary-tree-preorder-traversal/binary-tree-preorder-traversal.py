"""
title : 144. Binary Tree Preorder Traversal
source : https://leetcode.cn/problems/binary-tree-preorder-traversal
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


class Solution:
    """标记法

    用栈存储尚未遍历的数据
    栈顶数据出栈后，判断数据类型，TreeNode 类型的将其子节点和数据入继续入栈
    int 类型的添加到结果列表中， None 类型的跳过
    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [root], []
        while stack:
            element = stack.pop()
            if isinstance(element, TreeNode):
                stack.extend([element.right, element.left, element.val])
            elif isinstance(element, int):
                result.append(element)
        return result


class Solution3:
    """莫里斯遍历

    时间复杂度： O(n)
    空间复杂度： O(1)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    ans.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            else:
                ans.append(p1.val)
            p1 = p1.right
        return ans


class Solution2:
    """迭代

    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return ans


class Solution1:
    """递归

    时间复杂度： O(n)
    空间复杂度： O(n)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.preorder(root, ans)
        return ans

    def preorder(self, root, ans):
        if root is None:
            return
        ans.append(root.val)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)


if __name__ == "__main__":
    root = [1, None, 2, None, None, 3]
    root = create_binary_tree(root, 0)
    print(Solution().preorderTraversal(root))

    root = []
    root = create_binary_tree(root, 0)
    print(Solution().preorderTraversal(root))

    root = [1]
    root = create_binary_tree(root, 0)
    print(Solution().preorderTraversal(root))

    root = [1, 2]
    root = create_binary_tree(root, 0)
    print(Solution().preorderTraversal(root))

    root = [1, None, 2]
    root = create_binary_tree(root, 0)
    print(Solution().preorderTraversal(root))
