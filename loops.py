
# define a list to loop over

# names = ['Harry', 'Ron', 'Hermione']

# for name in names:
#     print(name)

name = 'Harry'

for character in name:
    print(character)

# H
# a
# r
# r
# y


person = [
    {'name': "harry", 'house': 'ravenclas',
     'name': 'rom', 'house': 'nice'}
]



person.sort(key=lambda person: person['house'])

print(person)
# n = [10, 32, 4, 12]

# this will get the entire length of the list

# print(len(n))
    
# prints 4 