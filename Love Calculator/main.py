# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
NAMES = name1 + name2
LOWERNAMES= NAMES.lower()
t=LOWERNAMES.count("t")
r=LOWERNAMES.count("r")
u=LOWERNAMES.count("u")
e=LOWERNAMES.count("e")
name1_add = t+r+u+e
l=LOWERNAMES.count("l")
o=LOWERNAMES.count("o")
v=LOWERNAMES.count("v")
e=LOWERNAMES.count("e")
name2_add = l+o+v+e
LoveScores = str(name1_add) + str(name2_add)
LoveScores =int(LoveScores)
if (LoveScores <= 10) or (LoveScores >= 90):
	print(f"Your score is {LoveScores}, you go together like coke and mentos.")
elif (LoveScores >= 40) and (LoveScores <= 50):
	print(f"Your score is {LoveScores} , you are alright together.")
else:
	print(f"Your score is {LoveScores}.")
	
# output : What is your name? 
chetan pujari
What is their name? 
Kriti Sanon
Your score is 62.
