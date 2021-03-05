file = open('file.txt', 'r') # The first parameter is the name of the file and the second is what you want to do with the file
                                # In this case, we want to read the file

f = file.readlines()

newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1]) # -1 goes to the last character but doesn't include it 
    else:
        newList.append(line)

# This removes the \n but easier
newList2 = []
for line2 in f:
    newList2.append(line.strip())

# Output is ['Hey\n', 'Bryan\n', 'Easy\n', 'hi\n', 'bye\n']
# The reason there's a \ in the between all the words is because we pressed Enter to break a line in the file
print(newList) 

