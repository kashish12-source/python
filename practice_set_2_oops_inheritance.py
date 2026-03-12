# '''program 1:
# wap with class 2D vectore and use that to create the 3D vector '''
   
# '''it is the concept of icap ,jCap ,kCap'''
# class C2d:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j
#     def __str__(self):
#         return f'{self.icap}i + {self.jcap}j'
# class C3d(C2d):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap=k
#     def __str__(self):
#         return f'{self.icap}i + {self.jcap}j + {self.kcap}k'
# v2d=C2d(1,2)
# v3d=C3d(1,3,3)
# print(v2d)
# print(v3d)



# '''program 2:
# create a class pet from animal and further create class dog from pet and add method bark to dog'''
# class Animal:
#     def show(self):
#         print('animals are the natural creature that are made before the humans')
# class Pet(Animal):
#     def type(self):
#         print('animals can be of two types:\npet animal\nwild animal')
# class Dog(Pet):
#     def bark(self):
#         print("bhow - bhow")
# a=Animal()
# p=Pet()
# d=Dog()
# a.show()
# p.type()
# d.bark()


'''program 3:
create a class employee and add salary and increment property to that write  a method salaryAfterIncrement with a porperty decorator
with a setter which changes the value of increment based on the salary'''
class Emp:
    salary=20000
    increment=5000
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,value):
        self.value=value
        self.increment = self.value-self.salaryAfterIncrement
e=Emp()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=500000
print(e.salary)
print(e.increment)









































