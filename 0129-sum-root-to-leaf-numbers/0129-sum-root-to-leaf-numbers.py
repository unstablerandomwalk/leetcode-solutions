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
            if not node:
                return 0
            create_num = (create_num * 10) + node.val
            if not node.left and not node.right:
                return create_num
            return helper(node.left, create_num) + helper(node.right, create_num)
        return helper(root,0)
