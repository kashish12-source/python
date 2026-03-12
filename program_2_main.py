'''we are going to write a program which will generate the random no. and we will ask the user to guess the no. and 
we tell the user whether the guess is correct or not and we will also tell the user whether the guess is too high or too low



since for this we will use the random module '''
import random
rand =random.randint(1,100)

userguess=None
guesses=0
while userguess!=rand:
    userguess=int(input('enter the number here :'))

    if userguess<rand:
        
        print('you guess the smaller number')
    elif userguess>rand:
        
        print('you guess the greater number')
    guesses+=1
print(f'you guess the right number in {guesses} guesses')

