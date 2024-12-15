print("Tippin Aint Easy! Lets Get You On Your Way 😎.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10% 12% 15% ?"))
people = int(input("How many people to split the bill? "))

print(f"Each Person Should Pay: $ {round(bill * (tip / 100 + 1) / people , 2)}")
goofy = input("Who Paid For It? (Insert Name)")
print(goofy + " You A Goofy 🤡🤡")
