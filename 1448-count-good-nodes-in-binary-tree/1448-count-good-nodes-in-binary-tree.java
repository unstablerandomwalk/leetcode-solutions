/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int dfs(TreeNode node, int max_so_far){
        if (node == null)
        return 0;
        int count = 0;
        if (node.val >= max_so_far)
        count = 1;
        max_so_far = Math.max(node.val, max_so_far);
        count += dfs(node.left, max_so_far);
        count += dfs(node.right, max_so_far);
        return count;
    }
    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
}}