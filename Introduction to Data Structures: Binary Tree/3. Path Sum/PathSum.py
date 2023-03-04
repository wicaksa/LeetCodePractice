# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # create a helper function in order to pass in the current sum
        def dfs(node, curSum):

            # base case if the tree given is empty
            if not node:
                return False

            # add current node value to the sum
            curSum += node.val

            # check if the node is a leaf node : doesn't have any children
            # check if current sum equals the target sum
            if not node.left and not node.right:
                return curSum == targetSum

            # if it's not a leaf node, run dfs on both left and right
            # return if either of them are true
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        # call function
        return dfs(root, 0)
