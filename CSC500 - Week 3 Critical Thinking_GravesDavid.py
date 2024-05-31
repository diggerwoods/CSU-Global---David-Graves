# Critical Thinking Week 3
print("Part 1: Cost of Meal at a Restaurant")
# Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant. 
    # The program should ask the user to enter the charge for the food and then calculate the
    # amounts with an 18 percent tip and 7 percent sales tax. 
    # Display each of these amounts and the total price.
# Step 1: Gather the charge for the food from the user.
food_charge = float(input("Please enter the charge for your food: $"))
# Step 2: Calculate the tip as 18% of the food charge.
tip18_amount = .18 * food_charge
# Step 3: Calculate sales tax at 7% of the food charge.
tax_amount = .07 * food_charge
# Step 4: Calculate total cost of food.
total_price = food_charge + tip18_amount + tax_amount
# Step 5: Display each amount and total price
print(f'Food charge: ${food_charge:.2f}')
print(f'Tip amount @ 18%: ${tip18_amount:.2f}')
print(f'Sales tax @ 7%: ${tax_amount:.2f}')
print(f'Total price: ${total_price:.2f}')
print('\n')
print("Part 2: Alarm time")
# Part 2: Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
    # If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
    # Write a Python program to solve the general version of the above problem. 
    # Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
    # Your program should output what the time will be on a 24-hour clock when the alarm goes off.
# Step 1: Have user input current time in hours.
current_time = int(input('Please enter the current time using hours 0-23: '))
# Step 2: Have user input how many hours to wait for the alarm.
hours_until_alarm = int(input('Please enter how many hours to wait until alarm: '))
# Step 3: Calculate the alarm time.
alarm_time = (current_time + hours_until_alarm) % 24
# Step 4: Display time when the alarm will go off.
print(f"Your alarm will go off at {alarm_time:02d}:00.")


