#problem is we wanna get interval just from 

# [65,90,97,122]

def caesar_cipher(word,num):
	answer = []
	for letter in word:
		older_ord = ord(letter)
		if older_ord>=65 and older_ord<=90 :
			if (older_ord+num) > 90 :
				sol = ((older_ord+num)%90)+64
				new_letter = chr(sol)
				#print(new_letter)
			else :
				new_letter = chr(older_ord+num)
		else :
			if (older_ord+num) > 122 :
				sol = ((older_ord+num)%122)+96
				new_letter = chr(sol)
			else :
				new_letter = chr(older_ord+num)

		answer.append(new_letter)

	return "".join(answer)


answer = caesar_cipher("Aa",4) 
print(answer)


