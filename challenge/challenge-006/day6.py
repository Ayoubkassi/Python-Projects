import random 
import re
from replit import clear

a = '''
 _
| |__
| |  \\
| '_  \\ 
| | | |
|_| |_| '''

print(a)
print("\nWelcome to Hangman\n\n")

state0 = '''


 +----+
 |    |     
      | 
      |
      |
      |
      |
=========
'''

state1 = '''


 +----+
 |    |     
 O    | 
      |
      |
      |
      |
=========
'''

state2 = '''


 +----+
 |    |     
 O    | 
 |    |
      |
      |
      |
=========
'''

state3 = '''


 +----+
 |    |     
 O    | 
/|    |
      |
      |
      |
=========
'''

state4 = '''


 +----+
 |    |     
 O    | 
/|\   |
      |
      |
      |
=========
'''

state5 = '''


 +----+
 |    |     
 O    | 
/|\   |
 |    |
      |
      |
=========
'''

state6 = '''


 +----+
 |    |     
 O    | 
/|\   |
 |    |
/     |
      |
=========
'''

state7 = '''


 +----+
 |    |     
 O    | 
/|\   |
 |    |
/ \   |
      |
=========
'''

states = [state0, state1, state2 , state3 , state4 , state5 , state6 , state7]
words = ["badr", "love" , "ufc","imt","javascript"]
word = words[random.randint(0,len(words)-1)]
wrong = 0


#here we will have a loop until he find the word
userWord = ["_ "]*len(word)
# print(len(userWord))

while "".join(userWord) != word :
    if wrong == 7 :
        print("End of Game you lose!")
        break
    letter = input("Guess a letter : ")

    if word.find(letter) != -1:
        clear()
        indices = [i.start() for i in re.finditer(letter , word)]
        # print(indices)
        for i in indices:
            userWord[i] = letter
        print("\n\n","".join(userWord),"\n")
        print(states[wrong])
    else:
        clear()
        wrong+=1
        print("\n\n","".join(userWord))
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        print(states[wrong])



if("".join(userWord) == word):
    print("You won Congrats 🎉🎉🎉.")



