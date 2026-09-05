class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op={'+','-','*','/'}
        comp=0
        for i in range(len(tokens)):
            if tokens[i] not in op:
                stack.append(int(tokens[i]))
            else:
                num2=stack.pop()
                num1=stack.pop()
                if tokens[i]=='+':
                    comp=num1+num2
                elif tokens[i]=='-':
                    comp=num1-num2
                elif tokens[i]=='*':
                    comp=num1*num2
                else:
                    comp=int(num1/num2)
                stack.append(comp)          
              
        return (stack[-1])        