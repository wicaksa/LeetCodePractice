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
    
    // create an array list to hold output values
    List<Integer> output = new ArrayList<>();
    
    public List<Integer> preorderTraversal(TreeNode root) {
        
        // base case: if the root node is null, return the output
        if (root == null) {

            return output;
        }
        
        // add the current node's value to the output
        output.add(root.val);

        // traverse the left node
        preorderTraversal(root.left);

        // traverse the right node
        preorderTraversal(root.right);
        
        // return the output
        return output;
    }
}