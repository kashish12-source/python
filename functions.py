'''wap to greet the user with the good morning using function '''
def greet(user):
    print("good morning "+user)
user=input('enter your name here ')
greet(user)
'''in python we have two types of function bultin and the user define bultin functions are sum range print etc'''

# create a functino to add two numbers
def summation(num1 , num2):
    return (num1+num2)

a=int (input('Enter the 1st number here: '))
b=int(input('Enter the 2nd number here: '))
summ=summation(a,b)
print(summ)



