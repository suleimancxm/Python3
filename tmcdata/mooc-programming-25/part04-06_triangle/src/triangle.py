# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        print("#" * size)
    else:
        print(character[0] * size)

def triangle(size):
    for i in range(1, size + 1):
    # You should call function line here with proper parameters
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3, "#")
