'''operator overloading 
operators in python will get overloaded using the dunder methods 
dunder methods are those which are written like the init method'''
class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print('addition')
        return self.num+ num2.num
    def __mul__(self,num2):
        print('mulitply')
        return self.num * num2.num

n1=Number(4)
n2=Number(3)
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)  