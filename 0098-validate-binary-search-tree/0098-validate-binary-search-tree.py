class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, lo, hi):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return check(node.left, lo, node.val) and check(node.right, node.val, hi)
        return check(root, float('-inf'), float('inf'))