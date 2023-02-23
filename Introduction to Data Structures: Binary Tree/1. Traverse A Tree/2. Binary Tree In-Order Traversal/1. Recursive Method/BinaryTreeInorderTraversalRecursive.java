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
    
    // In order traversal : left -> root -> right
    List<Integer> output = new ArrayList<>();
    
    public List<Integer> inorderTraversal(TreeNode root) {
        
        // base case: if left child node is null return output
        if (root == null) {
            return output;
        }
        
        // get value of the left child
        inorderTraversal(root.left);
        
        // get value of the root node
        output.add(root.val);
        
        // get value of the right node
        inorderTraversal(root.right);
        
        return output;
    }
}