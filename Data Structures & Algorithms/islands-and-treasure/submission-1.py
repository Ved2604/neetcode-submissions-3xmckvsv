from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf=2147483647
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col]==0:
                    queue.append((row,col))

        while queue:
            curr=queue.popleft()
            row=curr[0]
            col=curr[1]
            for delr,delc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nrow=row+delr
                ncol=col+delc
                if nrow<0 or nrow>=m or ncol<0 or ncol>=n:
                    continue
                if grid[nrow][ncol]==inf:
                    grid[nrow][ncol]=grid[row][col]+1
                    queue.append((nrow,ncol))
            

