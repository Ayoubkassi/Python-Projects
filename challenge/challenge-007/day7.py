#problem is we wanna get interval just from 

# [65,90,97,122]

def caesar_cipher_encryption(word,num):
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


def caesar_cipher_decryption(word,num):
	answer = []
	for letter in word:
		older_ord = ord(letter)
		if older_ord>=65 and older_ord<=90 :
			if (older_ord-num) < 65  :
				sol = 91 - (65%(older_ord-num))
				new_letter = chr(sol)
				#print(new_letter)
			else :
				new_letter = chr(older_ord-num)
		else :
			if (older_ord-num) < 97 :
				sol = 123 - (97%(older_ord-num))
				new_letter = chr(sol)
			else :
				new_letter = chr(older_ord-num)

		answer.append(new_letter)

	return "".join(answer)



print(caesar_cipher_decryption("qnuuxlxmnab",9))


# print("Welcome To Caesar Cipher Encryption\n")
# choice = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
# message = input("Type your message : \n")
# shift = int(input("Type the shift number : \n"))
# if choice == "encode" :
#     print(f"Here's the encoded result: {caesar_cipher_encryption(message, shift)}")
# else :
#     print(f"Here's the decoded result: {caesar_cipher_decryption(message, shift)}")



