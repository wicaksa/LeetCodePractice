# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS

        # create an empty array to store result
        res = []

        # create a queue
        queue = collections.deque()

        # add the root to the queue to initialize it
        queue.append(root)

        # while queue is not empty
        while queue:

            # get the length of the queue
            queueLength = len(queue)

            # create an empty array to store values at each level
            level = []

            # iterate through the length of queue (how many items are in this level)
            for i in range(0, queueLength):

                # pop the first item in the queue
                node = queue.popleft()

                # if that item is not null
                if node:

                    # append the value to the level array
                    level.append(node.val)

                    # append left child to the queue
                    queue.append(node.left)

                    # append right child to the queue
                    queue.append(node.right)

            # if level is not null, append it to the result
            if level:

                res.append(level)

        # return result
        return res
