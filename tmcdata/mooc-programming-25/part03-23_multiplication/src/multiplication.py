number = int(input("Enter a positive integer: "))
if number <= 0:
    print("Please enter a number greater than zero.")
else:
    i = 1
    while i <= number:
        j = 1
        while j <= number:
            print(f"{i} x {j} = {i * j}")
            j += 1
        i += 1