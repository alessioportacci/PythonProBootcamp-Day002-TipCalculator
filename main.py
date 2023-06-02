print("Wlcome to the tip calculator.")
total = float(input("What was the toal bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
#Total + tip
total += (total * tip) / 100
#Total each person
total /= people
print(f"Each person should pay: {round(total, 2)}$")
