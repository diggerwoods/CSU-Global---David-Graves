# This UML is designed to ask for how many users then ask that amount of users to choose their top 3 
# Personality Traits from a list. After receiving all user input, the program returns the top 3 aggregated choices
# from the team and dispalys them in descending order.

#Step 1 - Add contextual notes for design.

print("\n- program notes")
print("\n- Note 1: program will loop 2x after 'User Input 3' to capture 3 values -> then proceed")
print("\n- Note 2: program will loop (x) gathered at 'User Input 1', after proceeding from 'User Input 3' -> then proceed")

#Step 2 - Create the dictionary 'Common_Personality_Traits' to store the different pages within the flow.

Common_Personality_Traits = {
    "Display 1": ["How many team members are there?"],
    "User Input 1": ["Integer must be input (x)"],
    "Display 2": ["Enter your name"],
    "User Input 2": ["User keys in name"],
    "Display 3": ["Please select your top 3 Personality Traits you have from the following list:"],
    "User Input 3": ["User keys integer (must be on list)"],
    "Display 4": ["Top 3 aggregated answers are displayed in descending order"]
    }

#Step 4 - Create the display function that prints the names and numbers of pages in the prototype
# in sequential order with each page number increasing with each step.

page_number = 1
for category, items in Common_Personality_Traits.items():
    print(f"\n--- Page {page_number} ---")
    print(f"Page type: {category}")
    for item in items:
        print(item)
    page_number += 1

#Step 5 - Print total pages for design.
print("\n--- total pages in design ---")
print(page_number-1)