### --- While Loops --- ###

# while condition == True: #
#    do this
#    break

# You can set the variable of a while loop
loop = True
password = 3

# This is shorter than typing while loop == true:
while loop:
    name = input('How do you spell my name? ')
    if name == 'Bryan':
        print("Correct!!")
        loop = False
    else:
        print('Learn to spell my name!')
        break # The break keyword will check if you're in a loop and break out of it 
