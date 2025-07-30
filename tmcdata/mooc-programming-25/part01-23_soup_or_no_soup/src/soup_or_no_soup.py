# Write your solution here
name = input("Please tell me your name: ")
if name != "Jerry":
    portion = int(input("How many portions of soup? "))
    portion_price = 5.90
    total_portion_cost  = portion_price * portion
    print(f"The total cost is {total_portion_cost}")

print("Next please!")
