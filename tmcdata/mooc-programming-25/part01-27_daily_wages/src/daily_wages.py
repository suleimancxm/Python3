# Write your solution here
hrly_wage = float(input("Hourly wage: "))
working_hrs = float(input("Hours worked: "))
day = str(input("Day of the week: "))

daily_wages = hrly_wage * working_hrs
if day == "Sunday":
    daily_wages *= 2
print(f"Daily wages: {daily_wages} euros")