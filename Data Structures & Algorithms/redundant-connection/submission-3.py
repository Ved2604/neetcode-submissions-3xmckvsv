from collections import defaultdict,deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        adj=[[] for _ in range(1,n+2)]

        def bfs(start):
            visited=set()
            queue=deque()
            queue.append((start,None))
            visited.add(start)
            while queue:
                curr,parent=queue.popleft()
                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei,curr))
                    elif nei!=parent:
                        return True
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if bfs(u):
                return [u,v]

        return []                             


          

               
        


