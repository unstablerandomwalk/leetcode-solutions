# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = 0
        temp=head
        while temp:
            nodes +=1
            temp=temp.next
        if nodes < k:
            return head
        curr=head
        prev=None
        count=0
        while count==0 or count%k!=0:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            count+=1
        head.next = self.reverseKGroup(curr, k)
        return prev