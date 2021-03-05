### --- Chained Conditionals and Nested Statements --- ###

x = 2
y = 3

# Either conditions have to meet with the AND operator
if x == y or y = x:
    print('Yes!')

# Both conditions have to meet with the AND operator
if x == y and y = x:
    print('Yes!')

# Not reverses anything inside the paranthensis 
if not(y == x and x + y == 5):
    print("ran")
else:
    print('no')

### Note you can have many conditions nested 

if x == 2:
    if y == 3:
        print('x = 2, y = 3')
    else:
        print('x = 2, y != 3')
else:
    print('x != 2')