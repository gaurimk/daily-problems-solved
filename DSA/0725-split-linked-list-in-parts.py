# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        size = n // k
        extra_part = n % k

        result = []
        curr = head
        for i in range(k):
            part_size = size + (1 if i < extra_part else 0)

            if part_size == 0:
                result.append(None)
                continue
            part_head = curr

            for _ in range(part_size - 1):
                curr = curr.next
            next_part = curr.next
            curr.next = None

            result.append(part_head)
            curr = next_part
        return result