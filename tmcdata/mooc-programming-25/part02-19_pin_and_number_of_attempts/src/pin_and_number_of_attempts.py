# Write your solution here
pin = "4321"
attempts = 0

while True:
    code = input("PIN: ")
    attempts +=1
    if code == pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")
        