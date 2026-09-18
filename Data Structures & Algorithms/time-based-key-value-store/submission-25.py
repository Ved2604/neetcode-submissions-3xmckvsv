class TimeMap:

    def __init__(self):
        self.tm={}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key]=[]
        self.tm[key].append((timestamp,value))    

           
    def get(self, key: str, timestamp: int) -> str:
        arr=self.tm.get(key,[])
        low,high=0,len(arr)-1
        result=""
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid][0]<=timestamp:
                result=arr[mid][1]
                low=mid+1
            else:high=mid-1   
        return result
        
