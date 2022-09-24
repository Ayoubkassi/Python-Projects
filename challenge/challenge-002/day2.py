import math 

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
num_people = float(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
amount = (total_bill * ((100+percentage)/100) ) / num_people
amount = round(amount,2)
print(f"Each person should pay: ${amount}")