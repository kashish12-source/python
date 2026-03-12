'''property decorator is used while defineing the funciton it will act as an property instead of funciton 
when we have large no. of attributes at that time we use the property decorator:'''
class Emp:
    salary=2000
    bonous=500
    # totalsalary=we create the total salary as the property decorator
    @property
    def totalsal(self):
        return self.salary+self.bonous
    # this will return automatically after calculating on the basis of salary and bonous
    # since if we set the total salary so we need to manage the salary  and bonous a/c to total salary for this we create an another funtion
    # with the same name but with the setter property
    @totalsal.setter
    def totalsal(self,val):
        self.bonous=val-self.salary

e=Emp()
print(e.salary)
print(e.bonous)
print(e.totalsal)
e.totalsal=3555
print(e.salary)
print(e.bonous)
print(e.totalsal)

