import random    

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']                #list of letters,numbers,symbols  

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []                           							   #empty list to store the final password

for l in range(1,nr_letters + 1):                    					#for looping in the range of 1 to the end of the list(1 to letter+1)
  password.append(random.choice(letters))
  
for s in range(1,nr_symbols+1):
  password.append(random.choice(symbols))
  
for n in range(1,nr_numbers+1):
  password.append(random.choice(numbers))            					# 3 for loops for looping through the lists and appending the password list with the random choice
  
random.shuffle(password)    											#shuffling the letters,symbols,numbers in the password list

password1 = ""
for char in password:                									
  password1 += char                                                    

print(f"Your password is: {password1}")