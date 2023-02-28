# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Naive Solution

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        hashSet = set()

        pointerNode = head

        while pointerNode and pointerNode.next:
            if pointerNode in hashSet:
                return pointerNode

            hashSet.add(pointerNode)
            pointerNode = pointerNode.next

        return None
