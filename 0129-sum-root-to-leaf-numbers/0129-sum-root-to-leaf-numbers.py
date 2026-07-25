# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def helper(node, create_num):
            nonlocal total
            if not node:
                return
            create_num = (create_num * 10) + node.val
            if not node.left and not node.right:
                total += create_num
                return
            helper(node.left, create_num)
            helper(node.right, create_num)
        helper(root, 0)
        return total
