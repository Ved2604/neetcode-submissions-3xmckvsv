class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        visited=[[False]*n for _ in range(m)]
        queue=[]
        queue.append((sr,sc))
        visited[sr][sc]=True
        initial=image[sr][sc]
        image[sr][sc]=color
        while queue:
            node=queue.pop(0)
            row=node[0]
            col=node[1]            
            for delRow,delCol in [(-1,0),(0,1),(1,0),(0,-1)]:
                nRow=row+delRow
                nCol=col+delCol
                if nRow<0 or nRow>=m or nCol<0 or nCol>=n:
                    continue
                if image[nRow][nCol]==initial and not visited[nRow][nCol]:
                    visited[nRow][nCol]=True
                    image[nRow][nCol]=color
                    queue.append((nRow,nCol))
        return image            
        
        