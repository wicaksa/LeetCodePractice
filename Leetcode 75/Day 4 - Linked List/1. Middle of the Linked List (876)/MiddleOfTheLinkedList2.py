# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pointer approach (slow and fast pointer)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slowPointer = head
        fastPointer = head

        while fastPointer != None and fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        return slowPointer
