class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])

        def dfs(r,c):
            pacific=False
            atlantic=False
            stack=[(r,c)]
            visited=set()
            while stack:
                #print(stack)
                curr=stack.pop()
                visited.add(curr)
                row=curr[0]
                col=curr[1]
                if row==0 or col==0:
                    pacific=True
                if row==m-1 or col==n-1:
                    atlantic=True
                if pacific and atlantic:
                    #print(f"For r,c:{r,c} proven at {row,col}")
                    break    
                
                for delr,delc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nrow=row+delr
                    ncol=col+delc
                    #nei=(nrow,ncol)
                    if (nrow,ncol) in visited:
                        #print(f"Found {nei} in visited not traversing it again")
                        continue
                    if nrow<0 or nrow>=m or ncol<0 or ncol>=n:
                        continue
                    if heights[nrow][ncol]<=heights[row][col]:
                        stack.append((nrow,ncol))
            return pacific and atlantic
        result=[]
        for r in range(m):
            for c in range(n):
                #print(f" r:{r} c:{c} dfs:{dfs(r,c)}")
                #print(dfs(r,c))
                if dfs(r,c):
                    result.append([r,c])
        return result            


            
        