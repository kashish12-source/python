import random
'''the random module is used to generate random output for the computer's choice in the game.'''
def gamewin(comp,you):
    if comp==you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print('comp turn: snake(s) water(w) gun(g)')
rand=random.randint(1,3)
if rand==1:
    comp='s'
elif rand==2:
    comp='w'
elif rand==3:
    comp='g'
you=input('you turn: snake(s) water(w) gun(g)')
game=gamewin(comp , you)
print(f'computer chose {comp}')
print(f'you chose {you}')
if game==None:
    print('the game is a tie')
elif game:
    print('you win')
else:
    print('you lose')