# imports just one function from file
# from functions import square

# imports whole file
import functions

for i in range(10):
    # if you import whole file you must use dot notation if not you just just
    # use the square(i) function
    print(f"the square of {i} is {functions.square(i)}")