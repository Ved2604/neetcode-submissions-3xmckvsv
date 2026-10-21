# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        count=0
        while l1:
            num1+=10**count*l1.val 
            count+=1
            l1=l1.next
        count=0
        num2=0
        while l2:
            num2+=10**count*l2.val
            count+=1
            l2=l2.next
        print(num1,num2)     
        s=num1+num2
        print(s)
        l3=ListNode()
        new=l3
        while s!=0:
            print(s)
            digit=s%10
            new.val=digit
            s=s//10
            if s!=0:
                new.next=ListNode()
            else: 
                new.next=None    
            new=new.next 
        return l3


        