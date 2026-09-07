
class Solution:


    def bfs(self,row,col,visited:List[List[bool]],grid:List[List[str]]):
        n=len(grid)
        m=len(grid[0])
        queue=[]
        visited[row][col]=True
        queue.append((row,col))
        while queue:
            node=queue.pop(0)
            curr_row=node[0]
            curr_col=node[1]
            visited[curr_row][curr_col]=True 

            for delrow, delcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nrow=curr_row+delrow
                ncol=curr_col+delcol
                if nrow<0 or nrow>=n or ncol<0 or ncol>=m:
                    continue
                if grid[nrow][ncol]=="1" and not visited[nrow][ncol]:
                    visited[nrow][ncol]=True
                    queue.append((nrow,ncol))

    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for _ in range(n)]
        count=0
        for row in range(n):
            for col in range(m):
                if grid[row][col]=="1" and not visited[row][col]:
                    self.bfs(row,col,visited,grid)
                    count+=1
        return count