class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            #print(stack)
            while stack and t>stack[-1][1]:
                #print(f"Found a temperature higher than last stack element: {stack[-1]} at index:{i} and temp:{t}")
                result[stack[-1][0]]=i-stack[-1][0]
                #print(f" So the result becomes {result}")
                stack.pop()
            stack.append((i,t))    
        return result

        