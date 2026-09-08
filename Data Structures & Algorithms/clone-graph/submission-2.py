"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldTonew={}
        oldTonew[node]=Node(node.val)
        stack=[node]
        while stack:
            curr=stack.pop()
            for nei in curr.neighbors:
                if nei not in oldTonew:
                    oldTonew[nei]=Node(nei.val)
                    stack.append(nei)                    
                oldTonew[curr].neighbors.append(oldTonew[nei])
                
                    

        return oldTonew[node]           

            





        
        