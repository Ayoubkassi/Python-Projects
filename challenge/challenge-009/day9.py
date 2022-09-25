#create blackjack game

from replit import clear
import random

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()

if choice == 'n':
	clear()
	print("Good bye !!")
else :
	clear()
	print("Welcome to BlackJack Game\n")
	players={}
	players["user"]     = random.sample(range(0,11),2)
	players["computer"] = random.sample(range(0,11),2)
	#print(players)
	print(f"Your cards : {players['user']}")
	print(f"Computer's first card : {players['computer'][random.randint(0,1)]}")
	addCard = input("Type 'y' to get another card, type 'n' to pass : ").lower()
	if addCard == "y" :
		players["user"].append(random.randint(0,10))
	userSum     = sum(players["user"])
	computerSum = sum(players["computer"])

	print(f"Your final hand : {players['user']}")
	print(f"Computer's final hand : {players['computer']}")
	if userSum > computerSum and userSum < 21:
		print("You Win")
	elif userSum == computerSum :
		print("Equality")
	else :
		print("You lose")






