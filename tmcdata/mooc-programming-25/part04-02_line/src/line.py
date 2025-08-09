def line(length, char):
    if char == "":
        print("*" * length)
    else:
        print(char[0] * length)

if __name__ == "__main__":
    line(3, "%")
    line(7, "Sulaiman")
    line(4, "")