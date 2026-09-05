class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low,high=0,len(matrix)-1  
        
        while low<=high:     #inital low=0, high=2       low=2,high=2
            mid=low+(high-low)//2 #mid = 1               mid=2
            if matrix[mid][0]>target:  # 10>30  f      14 > 30 false 
                high=mid-1             #             
            elif matrix[mid][0]<target:#  10<30 t               14 <30   true 
                 low=mid+1              #  low=2              low= 3 loop break    
            else: return True
        ind=high                                  
        low=0
        high=len(matrix[high])-1
        while low<=high:
            mid=low+(high-low)//2
            if matrix[ind][mid]>target:
                high=mid-1
            elif matrix[ind][mid]<target:
                low=mid+1
            else: return True
        return False        



