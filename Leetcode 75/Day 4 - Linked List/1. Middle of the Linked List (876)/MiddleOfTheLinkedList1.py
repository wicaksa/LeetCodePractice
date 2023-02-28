# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Naive Solution

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input : head of linked list
        # output: return the middle node

        # odd case: middle is floor div of length + 1
        # even case: middle is floor div of length / 2

        # get the length of the node
        pointerNode = head
        length = 0

        while pointerNode != None:
            pointerNode = pointerNode.next
            length += 1

        # depending on whether it's even or odd calculate the middle
        middle = (int)(length // 2)

        # traverse the head x amount to the middle node
        while middle > 0:
            head = head.next
            middle -= 1

        # return the middle node
        return head
