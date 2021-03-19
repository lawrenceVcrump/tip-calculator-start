#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = input("please enter the full bill amount")
bill2 = float(bill)
percentage=input("what percentage tip would you like to give?")
percent = int(percentage)
people = input("how many people will split the bill?")
people2 = int(people)
full_split = (bill2 / people2) /percent
split_amount = round(float(full_split), 2)
print(f"with a bill of {bill} and {people} people in the group each person should pay {full_split} dollars toward the tip")