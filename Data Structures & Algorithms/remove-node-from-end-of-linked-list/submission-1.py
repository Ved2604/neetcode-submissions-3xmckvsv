# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length_ll=0
        node=head
        while node is not None:
            length_ll+=1
            node=node.next 
        #if length is 1 return a null node 
        if length_ll==1:
            node=None
            return node 
        #nth node from end is length_ll-n+1 node from start  
        target=length_ll-n+1
        if target==1:
            head=head.next
            return head
        count=0
        node=head
        while node is not None: 
            count+=1
            if count==target-1:
                node.next=node.next.next 
            else:
                node=node.next       
        return head
