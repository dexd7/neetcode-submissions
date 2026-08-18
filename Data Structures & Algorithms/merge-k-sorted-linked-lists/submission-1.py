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
            merged_list = []
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                merged_list.append(self.mergeLists(l1, l2))
            lists = merged_list
        return lists[0]
    def mergeLists(self, list1, list2):
        #merge two sorted linked lists
        cur = ListNode(0)
        dummy = cur
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next
