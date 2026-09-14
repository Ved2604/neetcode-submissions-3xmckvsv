from collections import defaultdict,deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[x for x in range(n+2)]
        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x

        for u,v in edges:
            if find(u)==find(v):
                return [u,v]
            else:
                pu=find(u)
                pv=find(v)
                parent[pv]=pu
        
        return []                    
        
                            


          

               
        


