# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the latter end
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Merge the two halves
        begin, latter = head, prev
        while latter:
            temp1, temp2 = begin.next, latter.next
            begin.next = latter
            latter.next = temp1
            begin = temp1
            latter = temp2


