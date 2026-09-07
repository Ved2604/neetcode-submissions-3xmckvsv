class Solution:
    
    
    
    
    def bfs(self, row,col,visited: List[List[bool]],grid:List[List[int]]) ->int:
        n=len(grid)
        m=len(grid[0])
        area=0
        queue=[]
        visited[row][col]=True
        queue.append((row,col))
        while queue:
            node=queue.pop(0)
            area+=1
            row=node[0]
            col=node[1]
            for delRow,delCol in [(-1,0),(0,-1),(0,1),(1,0)]:
                nRow=row+delRow
                nCol=col+delCol
                if nRow<0 or nRow>=n or nCol<0 or nCol>=m:
                    continue
                if grid[nRow][nCol]==1 and not visited[nRow][nCol]:
                    visited[nRow][nCol]=True
                    queue.append((nRow,nCol))   

        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for _ in range(n)]
        maxArea=0
        for row in range(n):
            for col in range(m):
                if grid[row][col]==1 and not visited[row][col]:
                    area=self.bfs(row,col, visited, grid)
                    maxArea=max(maxArea,area)
        return maxArea            