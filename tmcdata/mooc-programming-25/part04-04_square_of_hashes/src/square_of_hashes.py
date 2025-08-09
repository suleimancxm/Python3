# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        print("*" * size)
    else:
        print(character[0] * size)
def square_of_hashes(size):
    for _ in range(size):

    # You should call function line here with proper parameters
        line(size, "#")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
