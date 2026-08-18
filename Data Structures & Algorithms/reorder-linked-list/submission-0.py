# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        temp = []
        while curr:
            temp.append(curr)
            curr = curr.next
        l = 0
        r = len(temp)-1
        while l<r:
            temp[l].next = temp[r]
            l+=1
            if l>=r:
                break
            temp[r].next = temp[l]
            r-=1
        temp[l].next = None

