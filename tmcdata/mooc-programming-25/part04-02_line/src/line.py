# Write your solution here
def line(length, char):
    if length <= 0:
        return ""
    return char * length
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")