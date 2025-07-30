# Write your solution here
sentence = input("Please type in a sentence: ")

words = sentence.split()
for word in words:
    if word:
        print(word[0])