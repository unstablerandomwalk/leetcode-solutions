# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def maxDepth(node):
            if not node:
                return 0
            leftmax = maxDepth(node.left)
            rightmax = maxDepth(node.right)
            self.diameter = max(self.diameter, leftmax + rightmax)
            return 1 + max(leftmax, rightmax)
        
        maxDepth(root)
        return self.diameter
