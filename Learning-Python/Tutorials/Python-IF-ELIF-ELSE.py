#### --- IF/ELIF/ELSE --- ####

# The condition can be anything that can return a value (variables, strings, intergers etc)
if condition == True:
    do this
    # Indentation matters in this case

### --- Examples --- ###

age = input('Input your age: ')

# Converting the age variable to an int is important here
if int(age) <= 18:
    print("Hey, you\'re underage!")
else:
   print("Hey, you\'re older!")
    
height = input('What is your height? ')
height = int(height)

if height <= 4:
    print("You\'re too short too ride!")
elif height == 11:
    print("Jesus, you\'re tall!")
elif height >= 8:
    print("You\'re too tall!")
else:
    print('Enjoy the ride!')



