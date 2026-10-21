"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        mp1={}
        mp2={}
        node=head
        h2=Node(node.val)
        new=h2
        while node:
            if node.next:
                new.next=Node(node.next.val)
            else: 
                new.next=None    
            mp1[node]=new
            mp2[new]=node
            new=new.next
            node=node.next
        new=h2
        while new:
            old=mp2[new]
            new.random=mp1.get(old.random,None)
            new=new.next    
        
        return h2    

        