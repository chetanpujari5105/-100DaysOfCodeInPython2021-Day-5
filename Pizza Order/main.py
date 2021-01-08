# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
bill = 0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
	bill += 15
	if add_pepperoni == "Y" :
		bill += 2
		if extra_cheese == "Y":
			bill += 1

if size == "M" :
	bill += 20
	if add_pepperoni == "Y":
		bill += 3
		if extra_cheese == "Y":
			bill += 1


if size == "L":
	bill += 25
	if add_pepperoni == "Y" :
		bill += 3
		if extra_cheese == "Y":
			bill += 1
print(f"your total bill is {bill}")
# Small Pizza: $15
# Small Pizza: $15
# Medium Pizza: $20
# Medium Pizza: $20
# Large Pizza: $25
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# size = "L"
# add_pepperoni = "Y"
# add_pepperoni = "Y"
# extra_cheese = "N"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.




