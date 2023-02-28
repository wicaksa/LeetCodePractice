# Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

## Examples

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

## Constraints

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100

## Approach
1. The first approach is intuitive. First, we loop through the entire array in order to get the length of the linked list. Next, we just get the floor div of the length by 2 to give us the middle index. From here, we traverse the head until it reaches the middle node. Then we return the node. 
2. This approach requires to node pointers. One pointer will be a fast pointer that moves 2 nodes at a time while the other one is a slow pointer that moves 1 node at a time. By the time the first pointer goes out of bounds, the slower pointer will be at the middle node. We can just return the middle node at this point.

## Review & Evaluate
1. Time: 2 * O(N) Space: O(1)
2. Time: O(N) Space: O(1)