# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # intialize a list to keep values to return
        output = []

        def pot(node):
            # base case
            if node == None:

                return

            # root
            output.append(node.val)

            # left
            pot(node.left)

            # right
            pot(node.right)

        pot(root)

        return output
