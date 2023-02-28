/**
 * Definition for singly-linked list.
 * class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */

public class Solution {
    public ListNode detectCycle(ListNode head) {

        Set<ListNode> hashSet = new HashSet<>();
        ListNode pointerNode = head;

        // Check each node to see if node is in the hash set
        // If it is, we just return the node
        // If it is not, we add it to the hash set

        while (pointerNode != null && pointerNode.next != null) {
            if (hashSet.contains(pointerNode)) {
                return pointerNode;
            } else {
                hashSet.add(pointerNode);
            }
            pointerNode = pointerNode.next;
        }
        return null;
    }
}