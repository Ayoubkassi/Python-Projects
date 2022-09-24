print("******************************************************************")
print("        |        |        |        |        |        |        |   ")
print("--------|-----.=\"\"_;=.----|--------|--------|--------|--------|---")

fire   = "\U0001F525"
reward = "\U0001F381"
tornado =  "🌪"
# print(fire*5)

print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
action = input("You come to a lake. There is an island in the middle of the lake . Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
color = input("You arrive at the island unharmed. There is a house with 3 doors. One red , one yellow and one blue. Which door you choose? \n")

if color == "red":
	print(f"it's a room full of fire {fire*5}. Game over.")
elif color == "blue":
	print(f"You won congrats {reward*5}")
else:
	print(f"there is a tornado here {tornado*5}")
    