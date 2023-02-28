/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode middleNode(ListNode head) {

        ListNode pointer = head;
        int length = 0;
        int middle;

        while (pointer != null) {
            length += 1;
            pointer = pointer.next;
        }

        middle = (int) (Math.floorDiv(length, 2));

        while (middle > 0) {
            head = head.next;
            middle -= 1;
        }
        return head;
    }
}