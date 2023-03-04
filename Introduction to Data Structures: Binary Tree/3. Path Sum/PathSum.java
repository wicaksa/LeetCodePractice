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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        
        int currentSum = 0;
        
        return dfs(currentSum, targetSum, root);   
    }
    
    public boolean dfs(int currentSum, int targetSum, TreeNode node) {
        
        // base case where you are given an empty node
        if (node == null) {
            return false;
        }
        
        currentSum += node.val;
        
        // you are at a leaf node return the comparison of target and current sum
        if (node.left == null && node.right == null) {
            return (currentSum == targetSum);
        }
        
        return dfs(currentSum, targetSum, node.left) || dfs(currentSum, targetSum, node.right);
     }
    
    
}