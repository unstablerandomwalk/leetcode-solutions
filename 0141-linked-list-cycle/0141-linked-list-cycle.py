# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[]
        curr=head
        if head==None:
            return False
        if head.next==None:
            return False
        while curr:
            if curr in l:
                return True
                break
            l.append(curr)
            curr=curr.next
        return False
            