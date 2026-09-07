
class Solution:
    def bfs(self,row,col,visited:List[List[bool]],grid:List[List[str]])-> None:
        n=len(grid)
        m=len(grid[0])
        queue=[]
        queue.append((row,col))
        visited[row][col]=True
        while queue:
            node=queue.pop(0)
            row=node[0]
            col=node[1]
            for delRow,delCol in [(-1,0),(0,-1),(1,0),(0,1)]:
                nRow=row+delRow
                nCol=col+delCol
                if nRow<0 or nRow>=n or nCol<0 or nCol>=m:
                    continue
                if not visited[nRow][nCol] and grid[nRow][nCol]=="1":
                    visited[nRow][nCol]=True
                    queue.append((nRow,nCol))
        return            

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