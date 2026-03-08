# '''program 1 :
# wap to print the table of 9'''

# for i in range(1,11):
#     if(i<=10):  
#         print(i*9)
# '''program 2:
# wap to greet all the names that start with k in the list'''

# l=['kashish','ram','anuj','anurag','keshav']
# for name in l:
#     if name.startswith('k'):
#         print('hello',name)

# '''program 3:
# wap to print whether the number is prime or not'''
# num=int(input('enter the number:'))
# if num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             print(num,'is not a prime number')
#             break   
#     else:
#         print(num,'is a prime number')      

# '''program 4:
# wap to print the sum of first n natural numbers using while loop'''
# n=int(input('enter the number here :'))
# sum=0
# i=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

'''program 5
 in this program you have to find the factorial of the number using loop'''
# n=int(input('Enter the number you want the factorial of :'))

# fact=1
# while n>=1:
#     fact=fact*n
#     n=n-1
# print(fact)

'''program 6:
write a program to print the pattern of the start
# _ _ * _ _
# _ * * * _
# * * * * *
# '''
# n=3
# for i in range(3):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(n-i-1))

# # in this program the end is used to remove the extra line from the program which will happens after every print statement
# # in this program we can also use the extra loop for the space but by using the formula we have done it in a single for loop
 



# '''program 7
# wap to print the pattern 
# *
# **
# ***'''

# for i in range(4):
#     print('*'*i)

'''porgram 8
print the multiplication table in reverse order
'''
# for i in range(10,0):
    # this will not run properly in this case we need to provide the steps in the for loop which is -1 which prints in the reverse order
    # print(i*9)

# right way is 
for i in range (10,0,-1):
    print(i*9)
