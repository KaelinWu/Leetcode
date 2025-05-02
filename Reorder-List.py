# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        fast, slow = head, head
    

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            foward = curr.next
            curr.next = prev
            prev = curr
            curr = foward

        second, first = prev, head


        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2