#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_amoung =float(input('What is the total of your bill?'))
nunber_of_people =float(input('how many people are going to contribute?'))
tip = float(input('what percentaje of tip would you like to give, 10,12,15?'))

tips = tip/float(100)

total_to_pay = total_amoung + tips

PricePerPerson = total_to_pay /nunber_of_people

print(f'Each person should pay ${PricePerPerson}')