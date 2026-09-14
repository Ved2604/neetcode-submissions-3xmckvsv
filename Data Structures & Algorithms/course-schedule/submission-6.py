class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preqmap={x:[] for x in range(numCourses)}
        for u,v in prerequisites:
            preqmap[u].append(v)
        

        visited=set()

        def dfs_is_cycle(start,path=None):  # cycle detection for directed graph
            
            visited.add(start)
            if not path:
                path={start}
            for nei in preqmap[start]:
                if nei in path:
                    return True
                elif nei not in visited:
                    path.add(nei)
                    if dfs_is_cycle(nei,path):
                        return True
                    path.remove(nei)
            return False        



        for node in range(numCourses):
            if node not in visited:
                if dfs_is_cycle(node):
                    return False

        return True            


                     

        