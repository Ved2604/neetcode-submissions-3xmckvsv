class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        if nums[0]>0:
            return []
        for i,num in enumerate(nums):
            l,r=i+1,len(nums)-1
            while l<r:
                tSum=num+nums[l]+nums[r]
                if tSum>0:
                    r-=1
                elif tSum<0:
                    l+=1
                else: 
                    res.add((num,nums[l],nums[r]))
                    l+=1
                    r-=1

        res1=[]    
        for t in res:
          res1.append(list(t))
        return res1


        