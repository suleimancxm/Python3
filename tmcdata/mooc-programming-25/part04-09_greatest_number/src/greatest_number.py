# # Write your solution here
# # You can test your function by calling it within the following block
# if __name__ == "__main__":
#     greatest = greatest_number(5, 4, 8)
#     print(greatest)


# # The return value of a function

#  # Fuctions can also return values. For instances, the built-in Python function input returns an input string typed in by the user. The value returned by a function can be stored in a variable:
# word = input("Please type in a word: ")
# word = int(input("Please type in an integer: "))
# if word != int:
#     print("Please type in an integer number!")

#     # The functions you define yourself can also return values. To do this you need the return statement. For example, the following function my_sum returns the sum of its parameters:
# def my_sum(a, b):
#     return a + b
# # result = my_sum(2, 3)
# # (
# print(f"Sum: {result}")

# def ask_for_name():
#     name = input("What is your name? ")
#     return name
# name = ask_for_name()
# print(f"Hello there, {name}")

# The return statement ends the execution of the function immediately. The following is a nifty way to create a comparison function:

def smallest(a,b):
	if a < b:
		return a
	return b
print(smallest(3, 7))
print(smallest(5, 2))

# You can make use of the return statement even if the function doesn't return a value. Its purpose then is to end the execution of the function:

def greet(name):
	if name == "":
		print("???")
		return
	print(f"Hello there, {name}")

greet("Emily")
greet("")
greet("Mark")

# If the argument (which gets stored in the variable name) is an empty string, the function prints out ??? and exits.

# Hello there, Emily
# ???
# Hello there, Mark

# Using return values from functions

# We already know that the return values of function can be stored in variables:


def my_sum(a, b):
	return a + b

result = my_sum(3, 5)

# We already