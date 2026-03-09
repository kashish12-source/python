'''since we made a function with  some arguments but we does not pass any of the arg while calling the function the it will show an error 
so to avoid this we use the default parameter value which will be printed when no arguments are passed while calling the fucntion '''
def greet(name='stranger'):
    print('hello good morning '+name)
greet()

