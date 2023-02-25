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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        int queueLength; 
        
        TreeNode node;
        
        List<Integer> level; 
        
        List<List<Integer>> result = new ArrayList<>(); 
        
        Queue<TreeNode> queue = new LinkedList<>(); 
        
        queue.add(root);
        
        while (queue.size() != 0) {
            
            level = new ArrayList<>();
            
            queueLength = queue.size();
            
            for (int i = 0; i < queueLength; i ++) {
                
                node = queue.remove();
                
                // System.out.println(node.val);
                
                if (node != null) {
                    
                    level.add(node.val);
                    // System.out.println(level);
                    
                    queue.add(node.left);
                    
                    queue.add(node.right);
                }
            }
            
            if (level.size() != 0) {
                
                result.add(level); 
            }
            
            System.out.println("Result: " + result);
        }
        
        return result;
        
        
        
    }
}