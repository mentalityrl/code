# .strip(), len(), .lower(). .upper(), .split()

text = input('Input something: ')
print(text.strip()) # This removes the spaces in the returned input
print(len(text)) # This prints the length of the user input
print(text.lower()) # This prints the user input in lowercase
print(text.upper()) # This prints the user input in uppercase

# home.house.2.safe will print ['home', 'house', 2, 'safe']
print(text.split()) # .split removes the delimitor and makes a list


