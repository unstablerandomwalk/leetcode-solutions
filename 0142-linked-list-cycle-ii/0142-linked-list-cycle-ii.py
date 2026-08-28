# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = set()
        curr = head
        while curr != None:
            if curr not in h:
                h.add(curr)
            else:
                return curr
            curr = curr.next
        return None