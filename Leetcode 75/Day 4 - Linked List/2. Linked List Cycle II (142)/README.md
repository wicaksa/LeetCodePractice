# Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

## Examples 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

## Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

## Approach
1. For this approach, I used a hash set to keep track of the nodes I've seen. If the linked list loops back, it will eventually come to a node that we have already placed in the hash set. If the linked list ends, then the loop exits so we can just return None. 
2. This approach requires the use of two pointers. You have a slow pointer that moves 1 node at a time and a fast pointer that moves 2 nodes at a time. If the linked list is circular, the pointers should eventually meet up. If this happens, then there is a cycle. To find out which node is the entry point, we move the slow pointer back to the head and iterate each pointer by 1 node until they meet again.

## Review & Evaluate
1. Space: O(N) Time: O(N)
2. Space: O(1) Time: O(N)

## Follow up: Can you solve it using O(1) (i.e. constant) memory?
