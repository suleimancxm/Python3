def squared(text, size):
    length = len(text)
    for row in range(size):
        line = ""
        for col in range(size):
            # Calculate position in text with wrapping
            pos = (row * size + col) % length
            line += text[pos]
        print(line)

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)