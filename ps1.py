# part A - House Hunting: how long to save enough deposit
import numpy
import matplotlib

total_cost = float(input("what's the cost of your dream house? "))
portion_down_payment = 0.25
deposit = total_cost * portion_down_payment
annual_salary = float(input("what's your annual salary? "))
portion_saved = float(input("how much % would you save? decimal number please: "))
monthly_salary = annual_salary/12
r = 0.04 #annual_retun

month = 0
current_saving = 0
#should loop until current saving is enough for the deposit

while current_saving < deposit:

  current_saving = current_saving * (1 + r/12) + monthly_salary * portion_saved
  #by the end oh month_0,the beginning of month_1

  month += 1
  if month > 200:
    break

#print (month)
#print(current_saving)


#part b - saving with a raise: salary rises every 6 months

total_cost = float(input("what's the cost of your dream house? "))
portion_down_payment = 0.25
deposit = total_cost * portion_down_payment
annual_salary = float(input("what's your annual salary? "))
portion_saved = float(input("how much % would you save? decimal number please: "))
monthly_salary = annual_salary/12
r = 0.04 #annual_retun

semi_annual_raise = float(input("what the % pay rise? (decimal) "))


month = 0
current_saving = 0
#should loop until current saving is enough for the deposit

while current_saving < deposit:
  if month % 6 == 0 and month >0:
    monthly_salary = monthly_salary * (1 + semi_annual_raise)

  current_saving = current_saving * (1 + r/12) + monthly_salary * portion_saved
  #by the end oh month_0,the beginning of month_1

  month += 1
  if month > 300:
    break

#print (month)
#print(current_saving)

