# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1=head
        curr2=head
        while curr1 != None:
            try:
                curr1=curr1.next
                curr1=curr1.next
            except:
                continue
            curr2=curr2.next
        return curr2