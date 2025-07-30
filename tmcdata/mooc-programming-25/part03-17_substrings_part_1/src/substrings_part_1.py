user_input = input("Please type in a string: ")

for i in range(1, len(user_input) + 1):
    print(user_input[:i])  # Slice from start (0) up to i (exclusive)