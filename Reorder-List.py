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
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        second = slow.next
        slow.next = None
        node = None

        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp

        second = node
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2