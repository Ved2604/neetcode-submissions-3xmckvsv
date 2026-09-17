class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        #find the pivot first 
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        
        low,high=0,0
        if nums[l]<=target<=nums[-1]:            
            low=l
            high=len(nums)-1
        else:
            low=0
            high=l-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1                         




           
        