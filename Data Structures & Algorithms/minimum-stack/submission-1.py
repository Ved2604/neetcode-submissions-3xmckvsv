class MinStack:

    def __init__(self):
        self.li=[]
        self.ms=[]


        

    def push(self, val: int) -> None:
        self.li.append(val)
        val=min(val,self.ms[-1] if self.ms else val)
        self.ms.append(val)
       
        

    def pop(self) -> None:
        self.ms.pop()
        self.li.pop()
    
        

    def top(self) -> int:
        return self.li[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
