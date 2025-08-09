# Write your solution here
def spruce(size):
    print("a spruce!")

    for i in range(1, size + 1):
        spaces = " " * (size-i)
        stars = "*" * (2*i-1)
        print(spaces + stars)
    
    trunk_spaces = " "*(size-1)
    print(trunk_spaces + "*")

if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)