import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        #k should be between 1 to h 
        def calculate_time(k:int)->int:
            total=0
            for pile in piles:
                total+=math.ceil(pile/k)
            return total
        minimum=h    
        while low<=high:
            mid=low+(high-low)//2
            print(low,high,mid)
            total=calculate_time(mid)
            print(total)
            if total<=h:
                minimum=mid
                high=mid-1
            else:
                low=mid+1
        return minimum            



            


        