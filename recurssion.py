'''wap to print the factorial of the given no.'''

# '''since the normal factorial program using for loop is '''
# n=0
# product=1
# if(n==0):
#         product=0
# else:
#     for i in range(n):
    
#         product=product*(i+1)
# print (product)


'''since while using the function we create a factorial of the number '''

def factorial(n):
    product =1
    
    for i in range (n):
        product=product*(i+1)
    return product
n=int(input('enter the numbere here: '))
pro=factorial(n)
print(pro)

'''another way to find the factorial of the numbere '''
def fact(num):
    if(num==1)or(num==0) :
        return 1
    else:
        return num*fact(num-1)

num=int(input('enter the numbere here:'))
print(fact(num))
