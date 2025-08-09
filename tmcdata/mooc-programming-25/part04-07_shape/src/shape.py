def line(size, character):
    print(character * size)

def shape(size1, char1, size2, char2):
   
    for i in range(1, size1 + 1):
        line(i, char1)
    
   
    for _ in range(size2):
        line(size1, char2)

if __name__ == "__main__":
    
    print("Pattern 1:")
    shape(5, "X", 3, "*")
    
    print("\nPattern 2:")
    shape(2, "o", 5, "+")
    

    print("\nPattern 3:")
    shape(3, ".", 0, "")