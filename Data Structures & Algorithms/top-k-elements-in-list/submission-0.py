class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(num for num in nums)
        freq_list=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(freq_list[i][0])
        return result



