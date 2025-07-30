def chessboard(size):
    for row in range(size):
        line = ""
        for col in range(size):
            line += "1" if (row + col) % 2 == 0 else "0"
        print(line)

if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)