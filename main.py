#If the bill was $150.00, split between 5 people, with a 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("Please enter the bill generated $")
Number_of_people = input("Please enter the number of people")
tip = input("How much tip would you like to give? 10, 12, or 15?")
tip_as_percentage = int(tip)/100
total_tip_amount = float(bill)*tip_as_percentage
total_bill = float(bill) + total_tip_amount
bill_per_person = total_bill/int(Number_of_people)
final_amount = round(bill_per_person, 2)
print(f'each person should pay {final_amount}')
