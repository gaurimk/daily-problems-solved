# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0,head)
        curr = dummy 
        prefix = 0
        seen = {}
        while curr:
            prefix += curr.val
            seen[prefix] = curr
            curr = curr.next
        prefix = 0
        curr = dummy
        while curr:
            prefix += curr.val
            curr.next = seen[prefix].next
            curr = curr.next
        return dummy.next
