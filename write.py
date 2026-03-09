'''here we perfrom the writing in the file'''
# f=open('another.txt','w')
# f.write('this is the another file in which we  perform the task of writing in a file using python')
# f.close()
'''by using this the another.txt file has been created and the text has been written in it '''
# f=open('another.txt','a')
# f.write(' this is the appended line ')
# f.close()
# f=open('another.txt','rb')
# data=f.read()
# print(data)
# f.close()

'''with statement
it is the best way to open the file and close the file automatically '''
with open('another.txt') as f:
    data=f.read()
    print(data)