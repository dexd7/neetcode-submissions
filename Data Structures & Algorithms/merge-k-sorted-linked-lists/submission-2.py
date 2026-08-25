# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists)>1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]


    def merge(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val<list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            else:
                if list1:
                    curr.next = list1
                    return dummy.next
                else:
                    curr.next = list2
                    return dummy.next

