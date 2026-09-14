from collections import defaultdict,deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        components={i:{i} for i in range(1,n+1)}
        print(components)

        for u,v in edges:
            
            if components[u]==components[v]:
                
                return [u,v]
            else:
                components[u]=components[u] | components[v] 
                for nei in components[u]:
                    components[nei]=components[u]

        return []        




                            


          

               
        


