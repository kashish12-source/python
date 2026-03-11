# '''program 1:
# create a class  programmer to store all the details about the programmer working in microsoft'''
# class programmer:
#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
#     def getdetails(self):
#         print(f'name of the employee is : {self.name}')
#         print(f'product name of the employee is : {self.product}')



# employee1=programmer('kashish','open source cv')
# employee2=programmer('keshav','scratchbox')
# employee1.getdetails()
# employee2.getdetails()

# '''program 2 :
# write a class calculator to calculate the square and cube and squareroot of a number'''
# import math
# class calculator:
#     def __init__(self , choice):
#         self.choice=choice
#     def square(self):
#         print(f'the square of the number is {self.choice*self.choice}')
#     def cube(self):
#         print(f'the cube of the number is {self.choice*self.choice*self.choice}')
#     def square_root(self):
#         print(f'the square root of the number is: {math.sqrt(self.choice)}')

# choose=int(input('enter what you want to perform\n enter 1 for square \n enter 2 for cube\n enter 3 for squareroot '))
# if choose==1:
#     choice=int(input('enter the number here:'))
#     calc=calculator(choice)
#     calc.square()

    
# elif choose==2:
#     choice=int(input('enter the number here:'))
#     calc=calculator(choice)
#     calc.cube()
   
# elif choose==3:
#     choice=int(input('enter the number here:'))
#     calc=calculator(choice)
#     calc.square_root()
    
# else:
#     print('please enter the number')


# '''program 3 :
# create a class with attribute a and also create an object of that class and then try to change the attribute by directly using the object '''

# class Hii:
#     a=10
# # this is the class attribute 
# bye=Hii()
# bye.a=100
# print(Hii.a)

# print(bye.a)
# # the class attribute will not be changed when the instance attribute will be change with the same name of attribute

# '''program 4 :
# add the static method in program 2 to greet the user with hello:'''


# import math
# class calculator:
    
#     def __init__(self , choice):
#         self.choice=choice
#     def square(self):
#         print(f'the square of the number is {self.choice*self.choice}')
#     def cube(self):
#         print(f'the cube of the number is {self.choice*self.choice*self.choice}')
#     def square_root(self):
#         print(f'the square root of the number is: {math.sqrt(self.choice)}')
#     @staticmethod
#     def greet():
#         print('thanks for using:)\nhave a nice day ')


# choose=int(input('enter what you want to perform\n enter 1 for square \n enter 2 for cube\n enter 3 for squareroot '))
# if choose==1:
#     choice=int(input('enter the number here:'))
#     calc=calculator(choice)
    
#     calc.square()
#     calc.greet()

    
# elif choose==2:
#     choice=int(input('enter the number here:'))
#     calc=calculator(choice)
    
#     calc.cube()
#     calc.greet()
   
# elif choose==3:
#     choice=int(input('enter the number here:'))
#     calc=calculator(choice)
#     calc.square_root()
#     calc.greet()
    
# else:
#     print('please enter the number')


# '''program 4:
# wap with the class railway with the methods to book a ticket to get status and to get the fare information for running the indian railways'''
# class IndianRail:
    
#     def bookTicket(self):
#         name=input('enter your name here:')
#         age=int(input('enter your age:'))
#         contact=int(input('enter contact no.'))
#     def getStatus(self,trainNo,day):
#         self.trainNo=trainNo
#         day='monday'
#         if self.trainNo==day:
#             print('train is available today')
#         else:
#             print('train is not available')
    
#     def fair(self,trainName):
#         self.trainName=trainName
#         if self.trainName=='rajdhani':
        
#             print(f'fair of the train is {100} rupees')
#         elif self.trainName=='mahakal':
#             print(f'fair of the train is {400} rupees')
#         else:
#             print('enter the valid train')

# passange=IndianRail()
# choose=int(input('what you want to search \nenter 1 for Book the ticket\nenter 2 for get status of the train\nenter 3 for get info of fair\n'))
# if choose==1:
#     passange.bookTicket()
# elif choose==2:
#     day=input('enter the day here :')
#     passange.getStatus(day)
# elif choose==3:
#     trainName=input('enter the train name here\nselect from rajdhani or mahakal \n')
#     passange.fair(trainName)




# '''since this is the ,my way without using the init method now by using the init method:'''

# class IndianRail:
    
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
    
#     def getStatus(self):
#         print(f'name of the train is {self.name}')
#         print(f'seats available in the train is {self.seats}')
    
#     def fareInfo(self):
#         print(f'fare of the train is {self.fare}')

# passange=IndianRail('intercity express',234,20)
# passange.getStatus()
# passange.fareInfo()


'''program 5
check if we are able to change the name of the self by any random things'''
class check:
    def __init__(kashish,name):
        kashish.name=name
        
hello=check('kashish')
print(hello.name)
