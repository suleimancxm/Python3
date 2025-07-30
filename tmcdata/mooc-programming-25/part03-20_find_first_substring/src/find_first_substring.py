word = input("Please type in a word: ")
char = input("Please type in a character: ")

lindex = word.find(char)

if index != -1 and index <= len(word) - 3:
    print(word[index:index+3])
else:
    print()