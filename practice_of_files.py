# '''program 1 
# wap to read the data from the file poem.txt and find whether it contain the word twinkel or not'''
# files=open('poem.txt','r')
# a=files.read()
# f=False
# if 'twinkle' in a:
#     f=True
# b=a.count('twinkle')
# print(b)
# print(a)
# if f:
#     print('the word twinkle is present in the file')
# else:
#     print('word is not present in the file')
# files.close()


# '''program 2 :
# their is the game funtion which will return the high scoere of the game stored in hiscore.txt file and if the score is greater than the high score 
# than it will update the high score in the file
# '''
# # def game():
# #     return 34
# # score=game()
# # with open('game.txt')as f:
# #     higscore = int(f.read())
# # if higscore<score:
# #     with open('game.txt','w')as f:
       
# #         f.write(str(score))
# # sice this program will throw error when the game.txt is empty to avoid this we use this
# def game():
#     return 34
# score=game()
# with open('game.txt')as f:
#     hiscore=f.read()
# if hiscore =='':
#     with open('game.txt', 'w')as f:
#         f.write(str(score))
# elif int(hiscore)<score:
#     with open('game.txt','w')as f:
#         f.write(str(score))         

# '''program 3 
# wap to write a table form 2 to 20 and print that in the another file for the 13 year old child'''

# with open('table.txt','w') as f:
#     for i in range (2,21):
#         for j in range(1,11):
#             f.write(f'{i}x{j}={i*j}\n')

# '''program 4 :
# a file fconatin the donkey multiple times and you need to rep;ace the domkey with the #### ery time'''

# with open('donkey.txt','r')as f:
#     a=f.read()
# a=a.replace('donkey','###')
# with open('donkey.txt','w')as f:
#     f.write(a)

'''progra0m 5:
wap to change the more than one word which is present in the list from the txt file '''
word=['monkey','donkey','kaddu']
with open('donkey.txt')as f:
    content=f.read()
for words in word:
    content=content.replace(words,'####')
with open('donkey.txt','w')as f:
    f.write(content)





