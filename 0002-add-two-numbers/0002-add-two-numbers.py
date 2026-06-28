# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=l1
        num1=0
        num2=0
        i=0
        while curr:
            num1+= (curr.val * (10**i))
            curr=curr.next
            i+=1
        curr=l2
        i=0
        while curr:
            num2+= (curr.val * (10**i))
            curr=curr.next
            i+=1
        res=num1+num2
        head=ListNode(res%10,None)
        res=res//10
        curr=head
        while res>0:
            newNode=ListNode(res%10,None)
            curr.next=newNode
            curr=curr.next
            res=res//10
        return head