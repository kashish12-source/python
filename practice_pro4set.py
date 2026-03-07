s=set()
s.add(1)
s.add(20.0)
s.add("20")
print(len(s))



k={}
print(type(k))



'''program 5:
create an empty dictonary and allow 4 friends to enter their favourate language as value and usetkey as their 
name assume that the names are unique '''

# dict={}
# user1=input("enter the languae of the first friend: ")
# user2=input("enter the languae of the second friend: ")
# user3=input("enter the languae of the third friend: ")
# user4=input("enter the languae of the fourth friend: ")

# dict={
#     '1st':user1,
#     '2nd':user2,
#     '3rd':user3,
#     '4th':user4
# }
# print(dict)

'''since in this question we have assumed that the keys are unique if what if the keys are not unique
then it will print he samme name twice and visa versa for the value if the value is duplicate then the 
value will get printed twice'''


mydict={}
user1=input("enter the languae of the first friend: ")
user2=input("enter the languae of the second friend: ")
user3=input("enter the languae of the third friend: ")
user4=input("enter the languae of the fourth friend: ")

mydict={
    '1st':user1,
    '2nd':user2,
    '3rd':user3,
    '4th':user4
}
print(mydict.keys())




'''here we check that if we are abel to change the value of the list which is present in the set S'''
S={8,7,12,'kashish',[1,2]}
S.replace([1,3])