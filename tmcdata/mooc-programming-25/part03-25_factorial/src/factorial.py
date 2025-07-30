# Program to repeatedly calculate factorials

while True:
    number = int(input("Please type in a number: "))
    
    if number <= 0:
        print("Thanks and bye!")
        break  # Exit the loop
    
    # Calculate factorial
    factorial = 1
    current = 1
    while current <= number:
        factorial *= current
        current += 1
    
    print(f"The factorial of the number {number} is {factorial}")
