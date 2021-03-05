count = 0 
while True: 
    userName = input("Hello! Welcome to FaceSnap! \n\nUsername: ") 
    password = input("Password: ")
    count += 1
    if count == 3: 
        break #exit
    else:
        if userName == 'elmo' and password == 'blue':
            print('Correct!')
            break #they are in, exit loop
        else:
            print('password and/or username incorrect, ' + count + ' trys left.' )
            #tell them it is wrong and have them retry, stay in loop
