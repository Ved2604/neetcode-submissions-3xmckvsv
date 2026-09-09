from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        fresh=set()
        rotten=set()
        distance=[[-1]*n for _ in range(m)]
        queue=deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col]==2:
                    rotten.add((row,col))
                elif grid[row][col]==1:
                    fresh.add((row,col))
        for fruit in rotten:
            distance[fruit[0]][fruit[1]]=0
            queue.append(fruit)
        while queue:
            curr=queue.popleft()
            row,col=curr[0],curr[1]
            for delR,delC in [(0,1),(1,0),(0,-1),(-1,0)]:
                nrow=row+delR
                ncol=col+delC

                if nrow<0 or nrow>=m or ncol<0 or ncol>=n:
                    continue
                if grid[nrow][ncol]==1 and distance[nrow][ncol]==-1:
                    distance[nrow][ncol]=distance[row][col]+1
                    queue.append((nrow,ncol))         
        maxTime=0            
        for fruit in fresh:
            r,c=fruit[0],fruit[1]
            if distance[r][c]==-1:
                return -1
            else: maxTime=max(maxTime,distance[r][c])
        return maxTime        


        