# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail=head
        idx_map={}
        idx=0
        while tail:
            idx_map[idx]=tail
            idx+=1
            tail=tail.next
        left=0
        right=len(idx_map)-1
        while left<right:
            idx_map[left].next=idx_map[right]
            left+=1
            if left==right:
                idx_map[right].next=None
                break
            idx_map[right].next=idx_map[left]
            right-=1
            if left==right:
                idx_map[right].next=None
                break
            

            
        
        