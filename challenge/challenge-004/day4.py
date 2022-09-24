import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

result = [rock, paper , scissors ]

user_decision = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors\n"))
print(f"You choose : \n {result[user_decision]}")
boot_decision = random.randint(0,2)
print(f"boot choice is : \n {result[boot_decision]}")
if user_decision == boot_decision :
	print("No one Win u are equal")
elif (user_decision == 0 and boot_decision == 2) or ( user_decision == 1 and boot_decision == 0) or (user_decision == 2 and boot_decision == 1) :
	print("You One Congrats 🎉🎉🎉")
else:
	print("You lose!")

