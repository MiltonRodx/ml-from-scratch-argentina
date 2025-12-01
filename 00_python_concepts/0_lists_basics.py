print('Insert a string')
strInput = input('>')

# Get values of interest
length = len(strInput)
indexCharacterO = strInput.index('o')
charactah = input('Insert character in order to search its index> ')
print(f"Your string is composed by {length} characters")
print(f"The first character '{charactah}' is in position {strInput.index(charactah)}")
print(f"It appears {strInput.count(charactah)} times")