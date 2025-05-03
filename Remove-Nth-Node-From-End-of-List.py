# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        first = head
        second = head
   
        for i in range(n):
            first = first.next
        
        if first == None:
            return head.next
        if first == second:
            return None
        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head
        