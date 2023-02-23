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

        # initalize a stack with the root node
        stack = [root]

        # while the stack is not empty
        while stack:

            # pop the last item
            node = stack.pop()

            # if node is not None
            if node:

                # append the node value to the output
                output.append(node.val)

                # append right child to stack
                stack.append(node.right)

                # append left child to stack
                stack.append(node.left)

        return output
