'''the concept of obejct orriented programming will only increase the reuseability of the code
it benifical but also the complicated one programming task
it works on the DRY principle
means DO NOT REPEAT yourself
DRY principle is also implemented by the functions and functions are used to reduce the size of the code 
and also enabale the accuracy of the code'''

# classes are mere a blueprint the do not hold any memory for themselves
# objects are the worker of the class which holds memory to perform the task 
'''
classes will always be named by pascal case i.e EmployeeName
and methods are names using camelcase i.e  inFloat


why do we use opps:
We use OOP in Python to organize code into reusable objects and classes, making programs easier to manage, reuse, and maintain.


OBJECT:
object is the instanciation of the class
syntax of object :
variable name= class name()'''

'''wap to print the sum of two numbers :
'''
class summation:
    def sum(self):
        print( self.a+self.b)

summ=summation()  
'''in this line we have created the object '''
summ.a=12
summ.b=13
'''in line 30 and 31 we have created a valriable or instances which will hold the memory to perform the task using the object name '''
summ.sum()
'''
since if we want to model any porblem in oops 
we need to understand the problem and then
NOUN == >CLASS - EMPLOYEE

VERB==>METHOD - SALARY 

ADJECTIVE==>ATTRIBUTE - NAME ,AGE, SALARY

in the above problem we have to find the sum of two numbers'''


'''in oops we have two types of attributes :
1. class attribute: class attribute is the attribute which is shared by all the objects of the class
2. instance attribute: instance attribute is the attribute which is unique for each object of the class'''


# class attribute exampele
class Employee:
    company='google'
name= Employee()
Employee.name='kashish vishnoi'
print(Employee.name)
Employee.company='youtube'

print(Employee.company)



'''Instance attribute example'''
class College:
    salry=10000
kashish=College()
kashish.contact='7489619180'
kashish.address='344'

keshav=College()
keshav.contact='15647164645'
keshav.addrese='546'
print(kashish.salry)
'''since the salary is the class attribute it is shared by all the objects of the class and we can access it by using the object name or 
by using the class name'''
print(keshav.contact)
'''this will throw an error since the name is the instance attribute and it is unique for each object of the class and we cannot access it by
using the class name'''


'''SELF keyword
self is referce to the instance of the class and it is used to access the instance attributes and methods of the class
it is used to differentiate between the instance attributes and the local variables of the method
it is used to access the instance attributes and methods of the class


'''
class Emp:
    company='google'
    def salary(self):
        print('salary is 100k')
kashish=Emp()
kashish.salary()
'''since in this case we use the self in the function so it will print the vlaue of the funciton 
as when we write [kashish.salary() it is converted into --> Emp.salary(kashish)]'''
'''which means that one parameter is passed while calling the funtion and the function is written without self parameter
will throw an error hence we use the self parameter'''

'''STATIC method :
since when we define the function we need to pass the self parameter to it :
but when we dont need to convert the calling into className.methodName(objectName)'''
'''that time we use the static method :
syntax of the static method :
@staticmethod'''
class Greet():
    @staticmethod
    def greeting():
        print('good morning sir/mam')
hello=Greet()
hello.greeting()  # this will thorw an error but when we write the @staticmethod it will run properly



'''CONSTRUCTOR:
__ init__()method will run as soon as the object of the class has been created or run   it will run automatically  without calling for it 
 '''

class Mam:
    def __init__(self):
        print('hello mam')
kavya=Mam()
'''it will print hello mam without even calling it'''

'''we can also pass the parameters in the constructor and we can also assign the values to the instances '''

class Mam:
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
        # print('hello mam')
    def getdetails(self):
        print(f'name of the faculty is : {self.name}')
        print(f'salary of the faculty is :{self.salary}')
        print(f'company of the faculty is :{self.company}')
kavya=Mam('kashish',100,'google')
kavya.getdetails()

