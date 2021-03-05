# Slice operator

fruits = ['apples', 'pear', 'oranges']
text = 'Hello, I like python'

print(fruits[1]) # This will print the second item which is pear
print(text[1]) # Will grab the letter e 

print(text[0:5]) # This will print the first 5 letters in the string
print(text[:5]) # This is the same
print(text[2:]) # This will start at 2 and end at the end

print(text[::2]) # The step is 2, which will skip every 2 letters and print
print(text[3::2]) # The start is 3, The step is 2, which will skip every 2 letters and print
print(text[3:10:2]) # The start is 3, The stop is 10, The step is 2, which will skip every 2 letters and print

fruits.append('blueberrys')

# Lets say we want to add items to specific spots on the list
fruits[0:0] = 'a'
fruits[1:1] = 'b'
print(fruits[0:len(fruits)])