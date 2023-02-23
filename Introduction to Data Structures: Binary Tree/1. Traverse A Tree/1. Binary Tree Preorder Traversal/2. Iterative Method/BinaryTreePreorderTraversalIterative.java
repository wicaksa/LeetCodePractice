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
    
    public List<Integer> preorderTraversal(TreeNode root) {
        
        // create a list to hold the output
        List<Integer> output = new ArrayList<>();
    
        // create a stack to iteratively perform the operation
        Stack<TreeNode> stack = new Stack<>(); 
        
        // push root node to stack
        stack.push(root);
        
        while (!stack.empty()) {
            
            TreeNode node = stack.pop();
            
                if (node != null) {
                    // append value at node
                    output.add(node.val);

                    // add right right to the stack
                    stack.push(node.right);

                    // add left child to the stack
                    stack.push(node.left);
            }
        }

        return output;
    }
}
