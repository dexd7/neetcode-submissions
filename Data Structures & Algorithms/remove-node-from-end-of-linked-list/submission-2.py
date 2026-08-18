# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        dummy = head
        while dummy:
            nodes.append(dummy)
            dummy = dummy.next
        if len(nodes) == n:
            return head.next
        nodes[len(nodes)-n-1].next = nodes[len(nodes)-n+1] if len(nodes)-n+1 in range(len(nodes)) else None
        return head
        