class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        #region=set()
        def dfs(r,c):
            stack=[(r,c)]
            visited=set()
            boolean=True
            while stack:
                curr=stack.pop()                    
                row=curr[0]
                col=curr[1]
                if row in (0,m-1) or col in (0,n-1):
                    boolean=False
                    break    
                visited.add((row,col))
                for delr,delc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nrow=row+delr
                    ncol=col+delc
                    if nrow<0 or nrow>=m or ncol<0 or ncol>=n:
                        continue
                    if (nrow,ncol) in visited:
                        continue
                    if board[nrow][ncol]=="O":
                        stack.append((nrow,ncol))
            if boolean:
                for node in visited:
                    board[node[0]][node[1]]="X"
        for row in range(m):
            for col in range(n):
                if board[row][col]=="O":
                    dfs(row,col)



