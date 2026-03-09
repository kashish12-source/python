'''their are two types of files in python
text file which will open in notepad ex txt , .c ,.cpp,.py etc
and binary file which will open in media player ex .mp4, .mp3, .jpg etc
python have lots of fucntion for reading writing and updating the file 
open funtion of python
it is the predefiend function in python which is used to open the file in python 
syntax of open fuction is :
open(filename,mode)'''
'''mode means in which way you want to open the file read ,write or update 
'''
f=open('sample.txt','r')
# data=f.read(5) # it will read the first 5 characters of the file
# print(data)
# f.close()
# by default the mode is r
'''another function of reading a file is readline function which will read the only 1st line of the file'''
date=f.readline()
print(date)