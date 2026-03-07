'''wap to input eight numbers vfrom the vuser and display all the unique number'''
num1=int(input('enter the 1st number here:'))
num2=int(input('enter the 2st number here:'))
num3=int(input('enter the 3st number here:'))
num4=int(input('enter the 4st number here:'))
num5=int(input('enter the 5st number here:'))
num6=int(input('enter the 6st number here:'))
num7=int(input('enter the 7st number here:'))
num8=int(input('enter the 8st number here:'))

'''since to display the unique number we can not  use the dictonary because dictonary will have the duplicate
value and cannot print only the unique value so we will use the set data structure  to print the unique 
number as the set will print aor contain only the unique value '''


uniquenum={num1,num2,num3,num4,num5,num6,num7,num8}
print('the unique number are here ',uniquenum)
