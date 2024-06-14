# Part 1
def main():
    # Step 1: Ask user for the number of years
    num_years = int(input("Enter the number of years: "))

    total_rainfall = 0
    num_months = num_years * 12

    # Step 2: Create a loop for each year
    for year in range(1, num_years + 1):
        print(f"Year {year}:")
        for month in range(1, 13):
            # Step 3: Ask user for the inches of rainfall for the current month
            rainfall = float(input(f"Enter rainfall for month {month} (in inches): "))
            total_rainfall += rainfall

    # Step 4: Calculate and print average rainfall
    average_rainfall = total_rainfall / num_months

    print("\nResults:")
    print(f"Total months: {num_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches \n")

if __name__ == "__main__":
    main()

# Part 2
# Ask the user to enter the number of books purchased
number_of_books = int(input("Enter the number of books purchased this month: "))

# Initialize an empty message
message = ""

# Check if the input is valid (non-negative)
if number_of_books < 0:
    message = "Error. Enter a positive number and try again.\n"
else:
    # Determine the points based on the number of books
    if 0 <= number_of_books <= 1:
        message += "You have received 0 points this month."
    elif 2 <= number_of_books <= 3:
        message += "You have received 5 points this month."
    elif 4 <= number_of_books <= 5:
        message += "You have received 15 points this month."
    elif 6 <= number_of_books <= 7:
        message += "You have received 30 points this month."
    else: 8 <= number_of_books
        message += "You have received 60 points this month."

# Display the result
print(message)