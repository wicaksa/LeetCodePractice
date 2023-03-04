# Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

## Example

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

## Constraints

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

## Approach
In this problem, we conduct a dfs through the tree. We first check if the tree given is empty. If that's the case we simply return false. If there is a tree, we want to first add the value. Then, we need to check whether or not that tree is a leaf node meaning that it doesn't have any children. If this is true, we simply check the current sum of our traversal and compare it against the target sum. If we are not at a leaf node, that means we need to traverse some more. In this case, we traverse the left node and then traverse the right node. We will return true if any of these traversals result in a true value meaning that there is at least 1 path that equals the target value.

## Review & Evaluate
- Time: O(N) since we have to traverse the whole tree and check at worst all of the nodes.
- Space: O(N) or O(N log N) = height of the tree