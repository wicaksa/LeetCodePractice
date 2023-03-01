# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        # since we have a root, the minimum result will be 1
        # now we just traverse the left and right children to see which has a larger depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
