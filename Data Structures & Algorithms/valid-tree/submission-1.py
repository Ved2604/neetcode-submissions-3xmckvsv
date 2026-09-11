class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj={i:set() for i in range(n)}

        for e in edges:
            u=e[0]
            v=e[1]
            adj[u].add(v)
            adj[v].add(u)
            
               
        
        visited=set()
        def bfs_is_cycle(start):
            queue=deque([(start,None)])
            visited.add(start)
            while queue:
                curr,parent=queue.popleft()
                for nei in adj[curr]:
                    if nei in visited:
                        if nei!=parent:
                            return True
                    else:
                        visited.add(nei)
                        queue.append((nei,curr))
            return False

        for node in adj:
            if node not in visited:
                if bfs_is_cycle(node):
                    return False

        return True    


            
