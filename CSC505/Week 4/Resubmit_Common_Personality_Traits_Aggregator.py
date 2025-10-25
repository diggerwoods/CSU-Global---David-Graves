# This Common Personality Trait Program is designed to ask for how many users then ask that amount of users to choose 
# their top 3 Personality Traits from a list. After receiving all user input, the program returns the top 3 aggregated 
# choices from the team and dispalys them in descending order.

# Step 1: Define the function 'get_user_choices' to gather the top 3 choices from a user from a list of defined options.

def get_user_choices(preset_values):

    print("Please select your top 3 Personality Traits you have from the following list:")
    for i, value in enumerate(preset_values):
        print(f"{i+1}. {value}")
    
    choices = []
    while len(choices) < 3:
        try:
            choice = int(input("Enter a number: ")) - 1
            if 0 <= choice < len(preset_values):
                choices.append(preset_values[choice])
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
    return choices

def analyze_choices(user_data):
    
# Step 2: Calculates the most selected items from user data.
   
    choice_counts = {}
    for choices in user_data.values():
        for choice in choices:
            choice_counts[choice] = choice_counts.get(choice, 0) + 1
    
    sorted_counts = sorted(choice_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts[:3]

# Step 3: Gathers number of iterations to run the program and defines list choices for each user to choose from

if __name__ == "__main__":
    num_users = int(input("How many team members are there? "))
    preset_values = ["Individual Responsibility", "Acute Awareness", "Brutal Honesty", "Resilience Under Pressure",
                      "Sense of Fairness", "Attention to Detail", "Pragmatism"]
    user_data = {}
    
    for i in range(num_users):
        name = input(f"Enter your name (user {i+1}): ")
        user_data[name] = get_user_choices(preset_values)
    
# Step 4: Prints top 3 aggregated choices and displays associated tallies in descending order.

    top_choices = analyze_choices(user_data)
    print("\nTop 3 common personality traits of the team:")
    for choice, count in top_choices:
        print(f"{choice}: {count} votes")
