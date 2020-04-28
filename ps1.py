## part A - House Hunting: how long to save enough deposit
#import numpy
#import matplotlib
#
#total_cost = float(input("what's the cost of your dream house? "))
#portion_down_payment = 0.25
#deposit = total_cost * portion_down_payment
#annual_salary = float(input("what's your annual salary? "))
#portion_saved = float(input("how much % would you save? decimal number please: "))
#monthly_salary = annual_salary/12
#r = 0.04 #annual_retun
#
#month = 0
#current_saving = 0
##should loop until current saving is enough for the deposit
#
#while current_saving < deposit:
#
#  current_saving = current_saving * (1 + r/12) + monthly_salary * portion_saved
#  #by the end oh month_0,the beginning of month_1
#
#  month += 1
#  if month > 200:
#    break
#
##print (month)
##print(current_saving)
#
#
##part b - saving with a raise: salary rises every 6 months
#
#total_cost = float(input("what's the cost of your dream house? "))
#portion_down_payment = 0.25
#deposit = total_cost * portion_down_payment
#annual_salary = float(input("what's your annual salary? "))
#portion_saved = float(input("how much % would you save? decimal number please: "))
#monthly_salary = annual_salary/12
#r = 0.04 #annual_retun
#
#semi_annual_raise = float(input("what the % pay rise? (decimal) "))
#
#
#month = 0
#current_saving = 0
##should loop until current saving is enough for the deposit
#
#while current_saving < deposit:
#  if month % 6 == 0 and month >0:
#    monthly_salary = monthly_salary * (1 + semi_annual_raise)
#
#  current_saving = current_saving * (1 + r/12) + monthly_salary * portion_saved
#  #by the end oh month_0,the beginning of month_1
#
#  month += 1
#  if month > 300:
#    break
#
##print (month)
##print(current_saving)
#
##part c: finding the right amount to save away bisection search
#semi_annual_raise = .07
#r = .04
#total_cost = 1000000
#deposit = total_cost * .25
#annual_salary = float(input("what's your annual salary? "))
#monthly_salary = annual_salary / 12
#
#0 <= portion_saved <= 10000 #integer
#percentage = portion_saved / 10000 #four decimals
#
#months = 36
#diff = 100
#
#current_saving = 0
#
#def bisection(guess, target):
#  if guess == target:
#    print("guess")
#  elif guess < target:
#    # run the function to increase the guess
#    guess = (10000+guess)/2
#    bisection(guess2, target)
#  elif guess > target:
#    #run the function to lower the guess
#    guess = (0+guess)/2
#    bisection(guess,target)
#step = 0
#  month = 0
#  current_saving = 0
#    if month % 6 == 0 and month >0:
#      monthly_salary = monthly_salary * (1 + semi_annual_raise)
#
#    current_saving = current_saving * (1 + r/12) + monthly_salary * int(portion_saved)/10000
#    #by the end oh month_0,the beginning of month_1
#
#    month += 1
#    if month > 36:
#      break
#  bisection(current_saving,target)
#def current_saving (monthly_salary,portion_saved):
#  if
#
def current_saving(saving_portion=100):
  month = 0
  deposit = 1000000*.25
  monthly_salary = 150000/12
  current_saving = 0
  while current_saving < deposit:
    if month % 6 == 0 and month >0:
        monthly_salary = monthly_salary* (1 + .07)
    current_saving = current_saving * (1 + .04/12) + monthly_salary * (int(saving_portion))/10000
    month += 1
  #    print(month)
   #   print(monthly_salary)
    if month > 37:
      break
  return current_saving

saving = current_saving()
deposit = 1000000*.25
step = 0
saving_percentage = 100
while saving < deposit - 100:
  saving_percentage = int((saving_percentage + 10000)/2)
  saving = current_saving(saving_percentage)

  step +=1

  if step > 20:
    break

print("step: ",step)
print("saving: ",saving)
print("saving portion: ",saving_percentage/10000)

month = 0
deposit = 1000000*.25
monthly_salary = 150000/12
current_saving = 0
while current_saving < deposit:
  if month % 6 == 0 and month >0:
    monthly_salary = monthly_salary* (1 + .07)
  current_saving = current_saving * (1 + .04/12) + monthly_salary * 4411/10000
  month += 1
  #    print(month)
   #   print(monthly_salary)
  if month > 37:
    break
print(month)
print(current_saving)
