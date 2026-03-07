'''in this practice program we will create a python dictonary with hindi name and give the meaning
in the english language and allow the user to input the hindi words '''


mydict={
    'aam':'mango',
    'kela':'banana',
    'seb':'apple',
    'angoor':'grapes'
}
print('here is the all the keys of the dic',mydict.keys())
user=input('enter the hindi word here : ')
# print('the meaning of the word is here ',mydict[user])
# this line will show an error if the user enter the name which is not present in the dictonary


# but if you want to remove the error you need to use the get method which will not produce an error when the 
# user enter the word which is not present in the dict
'''the get method will bydefault print the none value and if you want to have the fallback value you can also give
that . the get method is not throw error because it works on the concept of if and else if the key found 
return key and if the key not found then return default value i.e is none or the fallback value'''
print('the ouput of the word is',mydict.get(user,'the word is not present in the dictonary'))
