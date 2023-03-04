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
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }
    
    // helper function that takes in two nodes
    // similar to using two trees to solve the problem
    public boolean isMirror(TreeNode t1, TreeNode t2) {
        
        // base case: if the tree nodes are both null return true
        // this means that trees are mirror images
        if (t1 == null && t2 == null) {
            return true;
        }
        
        // base case: if one of them is null return false
        // this means that the trees are not mirror images
        if (t1 == null || t2 == null) {
            return false;
        }
        
        // return the values of t1 and t2 && recursive of t1 left and t2 right
        return (t1.val == t2.val) && isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left) ;
    }
}