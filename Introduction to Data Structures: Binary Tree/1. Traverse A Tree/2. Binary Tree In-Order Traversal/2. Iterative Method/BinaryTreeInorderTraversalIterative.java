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
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> output = new ArrayList<>(); 
        
        Stack<TreeNode> stack = new Stack(); 
        
        TreeNode currentNode = root;
        
        while (!stack.empty() || currentNode != null) {
            
            // Traverse the left node until you are not able to
            while (currentNode != null) {
                
                stack.push(currentNode);
                
                currentNode = currentNode.left;
            }
            
            currentNode = stack.pop();
            
            output.add(currentNode.val);
            
            currentNode = currentNode.right;
        }
        
        return output;
        
    }
}