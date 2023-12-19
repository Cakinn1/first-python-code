# going to get info
import sys


try: 
    # try this (basically numbers if user has typed in a number)
    x = int(input("x: "))
    y = int(input("y: "))
    # if user types in a word we will call valueError which python literally
    # tells us to call
except ValueError:
    #print error
    print('Error: Invalid input.')
    # exit block of code with a status code of 1
    sys.exit(1)

# throw errors when something unexpected occurs

# we try to do this result
try:
    result = x / y
# but if an error occurs (cannt divide by 0 error)
except ZeroDivisionError:
    print('Error: cannot divde by 0')
    # this will exit the program basically a break? in js
    # and we will exit with a status code of 1
    sys.exit(1)
print(f"{x} / {y} = {result}")

    
# remember in the terminal python literally tells you whats going on i.e 
# python is telling me before doing this try and expect call that we are 
# having a ZeroDivisionError.
    



