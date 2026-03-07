# '''find the number greatest among all the four no.'''
# num1=int (input('enter 1st number:'))
# num2=int (input('enter 2st number:'))
# num3=int (input('enter 3st number:'))
# num4=int (input('enter 4st number:'))


# if(num1>=num2 and num1>=num3 and num1>=num4):
#     print('greatest number is:',num1)
# elif(num2>=num1 and num2>=num3 and num2>=num4):
#     print('the greatest number is :',num2)
# elif(num3>=num1 and num3>=num2 and num3>=num4):
#     print('the greatest number is :',num3)
# else:
#     print('the greatest number is :',num4)


# '''now the practice program 2 is :
# wap to find out wher=ther a student is pass or fail if it requires total 40%anf at least 33%in eafch subject to pass .
# assume that their are 3 subjects and take marksa as an input from the user '''
# print('enter marks of each subject in percentage ')
# sub1=int(input('Enter the marks of 1st subject:'))
# sub2=int(input('Enter the marks of 2st subject:'))
# sub3=int(input('Enter the marks of 3rd subject:'))

# if((sub1>=40 and sub2>=40 and sub3>=40)or (sub1>33 and sub2>33 and sub3>33)):
#     print('student is pass')
# else:
#     print('student is fail')


# '''third problem
# a span comment is defined as a text conating following keywords :
# write a program to delete this spans'''
# text=input('enter the text')
# spam=False
# if('make a lot of money' in text):
#     spam=True
# elif('buy now 'in text):
#     spam=True
# elif('subscribe this 'in text):
#     spam=True

# if (spam):
#     print('the text is spam')
# else:
#     print('the text is perfect')

# k

'''program 5
wap to check whether the entered name is in the list or not'''
l1=['kashish','ram','anuj','anurag','keshav']
user=input('enter the name here:')
if(user in l1):
    print('the is present in the list')
else:
    print('name is not present in the list')