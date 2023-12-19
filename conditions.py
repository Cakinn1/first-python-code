n = int(input('Number: '))

# we are checking if n is > 0 if that is we print n is positive

# elif means else if, elif n < 0 we print n is not a positive

# else n is zero

# before running this we must convert the n statement into a int else we will be just
# checking if a '5' > 0 which makes 0 sense since strings cant be calc like that 
# so we must use the int() function which is a python built in method which convert the string
# into a number
# also int takes in an argument which is almost always (i think) a string.

if n > 0:
    print('n is positive')
elif n < 0:
    print('n is not positive')
else: 
    print('n is zero')
    
# below is exactly what the code below is saying in javscript
# this is also assuming that we convert n into a number :-0 

# if(n > 0) {
#     console.log('n is positive')
# } else if(n < 0) {
#     console.log('n is not positive')
# } else {
#     consle.log('n is zaero')
# }