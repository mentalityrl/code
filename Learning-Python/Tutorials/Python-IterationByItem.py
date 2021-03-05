fruits = ['apples', 'pears', 'strawberry', 8, 90, 100]

# This goes through the entire list 
for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')

# This is a bit more refined because you can specify how many interations to go through
for x in range(0, 6):
    if fruit[x] == 'pears':
        print(fruits[x])
    else:
        print('not a pear')

# This is the same but iterates by the lenght of fruit which is 6
for x in range(len(fruits)):
    if fruit[x] == 'pears':
        print(fruits[x])
    else:
        print('not a pear')