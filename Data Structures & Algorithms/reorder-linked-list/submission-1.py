# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        nodes = []
        while dummy:
            nodes.append(dummy)
            dummy = dummy.next
        l = 0
        r = len(nodes)-1
        while l<r:
            nodes[l].next = nodes[r]
            l+=1
            if l==r:
                break
            nodes[r].next = nodes[l]
            r-=1
        nodes[l].next = None