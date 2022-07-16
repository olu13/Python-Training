#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_in_decimal = int(percentage_tip) / 100
people_to_split = input("How many people to split the bill? ")
total_bill_plus_tips = (tip_in_decimal + 1) * int(total_bill)
bill_per_person = round(total_bill_plus_tips / int(people_to_split) , 2)

print(f"Each person should pay: {bill_per_person}")