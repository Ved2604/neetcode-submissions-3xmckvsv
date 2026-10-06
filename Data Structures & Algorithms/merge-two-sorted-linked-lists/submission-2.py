# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start1=list1
        start2=list2 
        if list1 is None:
            return list2
        if list2 is None:
            return list1    
        while list1 and list2:       
            if list1.val<list2.val:
                temp=list1.next
                if temp is None:
                    list1.next=list2
                    break
                list1.next=list2 if list2.val<=temp.val else temp
                list1=temp
            else: 
                temp=list2.next
                if temp is None:
                    list2.next=list1
                    break
                list2.next=list1 if list1.val<temp.val else temp
                list2=temp
        return start1 if start1.val<start2.val else start2        

        