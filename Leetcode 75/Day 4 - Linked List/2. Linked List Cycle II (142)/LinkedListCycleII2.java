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

        ListNode s = head;
        ListNode f = head;

        // while fast node and fast node next are valid
        while (f != null && f.next != null) {

            // increment slow node by 1 and fast node by 2
            s = s.next;
            f = f.next.next;

            // check if fast node == slow node -> there is a cycle
            if (s == f) {

                // if there is a cycle, reset slow node to head and move each node by 1 until
                // they are the same
                s = head;
                while (s != f) {
                    s = s.next;
                    f = f.next;
                }
                return s;
            }
        }
        // return null
        return null;
    }
}