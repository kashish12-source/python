# '''inheritance is the way of creating a new class from the already existing class
# sytax of inheritance in python is
# name of the derived class(name of the parent class)'''
# class Employee:
#     company='microsoft'
#     def greet(self):
#         print(f'hello user weclome to {self.company}')
#         # this is the parent class 
# class Coustmer(Employee):
#     state='MP'
#     def city(self):
#         print(f'the city of the coustmer is indore')


# e=Employee()
# e.greet()

# # e.city() this will throw an error because the parent class cannot access the methods of the child class
# Employee.company

# # Employee.state this will also throw an error



# c=Coustmer()
# c.greet()
# c.city()
# Coustmer.state
# Coustmer.company
# ''' and this is called inheritance '''
# '''we have 3 types of inheritance in python:
# single inheritance--> When the child class will have only one parent 
# multiple inheritance--> when child class will have more than one parent class
# i.e:
# class A ,class B , class C 
# these are the three classes and apart from this their is the fourth class i.e class D
# class D is the child of A,B,C and this is called the multiple inheritance
# multilevel inheritance --> when the child class's parent is the also the child of the another class
# i.e:
# class A-->class B-->class C
# class B is child of class A and class B is the parent of class C 
# this is call the multilevel iheritance '''



# '''multiple inheritance'''
# class A:
#     def first(self):
#         print('I am from class A ')
# class B: 
#     def second(self):
#         print('I am from class B')
# class C (A,B):
#     def third(self):
#         print('I am the child of class A and class B ')

# # now we creat the obje of the class C
# obj=C()
# obj.first()
# obj.second()
# obj.third()

# # here we have created the object of class B
# sec=B()
# sec.second()
# # sec.third() this throw error because third is the method of class C and class is child of the B 
# # sec.first() this will also throw error because first is the method of class A and B is not a parent of A 

# fir=A()
# fir.first()
# # fir.second() this will throw error
# # fir.third() this will throw error



# '''example of multilevel inheritance:'''

# class A:
#     def first(self):
#         print('I am from A')
# class B (A):
#     def second(self):
#         print('I am from B')
# class C(B):
#     def third(self):
        
#         print('I am from C')


# obj=C()
# obj.third()
# obj.first()
# obj.second()
# ''' by using the object of class C we can access all the methods because  C is the child of B and B is the child of A  so , according to this A is the 
# parent of C'''


# obj2=B()
# # by using this object we can only access the methods of A and B we cannot access C
# # obj2.third()
# obj2.first()
# obj2.second()
# #  and from the obj of A we can only access the methods of A 


# '''super keyword:
# it is used to access the methods and attributes of the super class or the previous class of the existing class '''
# '''for example:'''

# '''since we can also use the super key word with the init funciton'''

# class A:
#     def __init__(self):
#         print("I am initializing A")
#     def first(self):
#         print('I am from A')
# class B (A):
#     def second(self):
        
#         print('I am from B')
# class C(B):
#     def third(self):
#         # now we use sper keyword with the init funtion:
#         super().__init__()
#         super().second()
#         # this will run the second method before pirnting the existing content of the second method 
#         print('I am from C')

# # it will print i'am initializing A twice as first coze of object and second coze of supper keyword
# obj=C()
# obj.third()
# obj.first()
# obj.second()


'''class method:
class method is used to change the orignal value of the class attribute:'''
class hello:
    time='morning'
    date=12
    year=2030
    
    # def times(self,tim):
    #     self.__class__.time=tim
    @classmethod
    def times(cls,tim):
        cls.time=tim
    
e=hello()
print(e.time)
print(e.date)
print(e.year)
e.times('sunday')
print(e.time)
print(hello.time)
# this will not change the value permanently so to perform this task we use two way 1.self.__class__.time=tim and 2] using class method

















