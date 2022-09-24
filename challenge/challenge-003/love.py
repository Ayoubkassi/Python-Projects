love = "\U0001F497"
print(f"{love*3}Welcome to the love Calculator{love*3}\n")
name1 = input("What is your name : ").lower()
name2 = input("What is their name : ").lower()

first = "true"
second = "love"

sum1 = 0
sum2 = 0

for letter in second:
	sum1+= name1.count(letter)
	sum1+= name2.count(letter)

for letter in first:
	sum2+= name1.count(letter)
	sum2+= name2.count(letter)

result = (sum2*10) + sum1

print(f"Love score = {result} {love*2}")

