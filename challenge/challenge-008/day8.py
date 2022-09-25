from replit import clear

data = {}
print("Welcome to the secret auction program.")
repeat = "yes"

while repeat == "yes":
    name = input("What is your name? : ")
    bid  = int(input("What's your bid? : $"))
    data[name] = bid 
    repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()


#pick up winner

winner = ""
maxBid = 0
for user in data:
	if data[user] > maxBid :
		maxBid = data[user] 
		winner = user

print(f"The winner is {winner} with a bid of {maxBid}$.")


