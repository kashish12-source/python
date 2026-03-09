# ''' wap to find the greatest of all using function '''

# def greatest(num1,num2,num3):
#     if(num1>=num2 & num1>=num3):
#         return num1
#     elif(num2>=num1 & num2>=num3):
#         return num2
#     else:
#         return num3


# num1=int(input('enter the 1st number :'))
# num2=int(input('enter the 2st number :'))
# num3=int(input('enter the 3st number :'))
# print('the greatest number among the all three is: ',greatest(num1,num2,num3))




'''wap using fucntion to convert the celcius to feranite : '''

# def converter(c):
#     return c*(9/5)+32


# c=float(input('enter the tempurature in celcious here:'))
# print('the ferehnite of the entered tempurature is : ',converter(c))

# '''how do prevent the python print function from printing the extra line at the end'''
# print('hello i am kashish: ',end='')
# print('he is my father: ')

'''write a recurrsive fucntion to find the sum of first n natural numbers'''

# def sum(n):
#     if(n==1):
#         return 1
#     return n+sum(n-1)
# n=int(input('enter the number here:'))
# print('the sum of n natural number is :',sum(n))


'''wap using fucntion to print the following pattern :
***
**
*


'''
# def pattern(n):
#     for i in range (n,0,-1):
#         print('*'*i)
# n=int (input('enter the number of rows here:'))
# print('the pattern is \n')

# pattern(n)

'''wap to convert inches to cm'''
# def measur(n):
#     return n*2.54
     
# n=float(input('enter the inches here :'))
# print('the inches of the entered number is :',measur(n))
'''
wap to remove a word from the list and then strip it at the same time'''

'''strip means removing the extra spaces in starting and ending fo the string 
since in this program we need to rplace the word with the blanke
'''

def remove_and_split(string , word):
    # since this program will replace the entered word with the space 
    newstr=string.replace(word,"")
    return newstr.strip()



th='     hello I am kashish vishnoi      '
n=remove_and_split(th , 'kashish')
print(n)