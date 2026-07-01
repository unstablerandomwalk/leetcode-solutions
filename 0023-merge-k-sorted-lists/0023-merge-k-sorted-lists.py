# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        val = []
        for head in lists:
            if head:
                node.append(head)
                val.append(head.val)

        dummy = ListNode(0)
        curr = dummy
        while node:
            m = min(val)
            i = val.index(m)
            curr.next = node[i]
            curr = curr.next
            node[i] = node[i].next
            if node[i]:
                val[i] = node[i].val
            else:
                node.pop(i)
                val.pop(i)

        return dummy.next