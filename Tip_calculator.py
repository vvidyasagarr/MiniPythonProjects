#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator")

bill1 = input(print("what is the total bill?"))
bill = int(bill1)
percentage_tip1 = input(print("what percentage tip would you like to give?"))
percentage_tip = int(percentage_tip1)
numOfPeople1 = input(print("how many people are splitting the bill?"))
numOfPeople = int(numOfPeople1)
each_person = ((bill/numOfPeople)+((percentage_tip*bill)/numOfPeople))

e = int(each_person)
print(e)

