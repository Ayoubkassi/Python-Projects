import random 

print("Welcome to the PyPassword Generator!")
name = input("Enter the name of website : ")
letters_len = int(input("How many letters would you like in your password?\n"))
symbols_len = int(input("How many symbols would you like?\n"))
numbers_len = int(input("How many numbers would you like?\n"))


password = ""



#add letters
for i in range (letters_len):
	maj_min = random.randint(0,1)
	if maj_min == 0 :
	    password+=chr(random.randint(65,90))
	else :
		password+=chr(random.randint(97,122))

#add numbers
for j in range (numbers_len):
	password+=str(random.randint(0,9))

#add symbols
for k in range(symbols_len):
	password+=chr(random.randint(0,64))



pass_list = list(password)
random.shuffle(pass_list)
result = ''.join(pass_list)

with open("passwords.txt",'w',encoding = 'utf-8') as f:
   f.write(f"{name}  :  {result}\n")
   f.close()


print(f"Here is your password : {result}")

