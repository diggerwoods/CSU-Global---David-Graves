#This program flow is designed to capture items and their paired quantities keyed by the user.

#Step 1 - Add contextual notes for design.

print("\n- program flow notes -")
print("\n- Note 1: if item name is entered in 'User Input 1' the program moves to 'User Input 2' screen for qty entry then loops back to 'User Input 1'")
print("\n- Note 2: if 'done' is entered in 'User Input 1' the program moves to 'Display 2' screen")

#Step 2 - Create the dictionary 'shopping_list' to store the different pages within the flow.
#Step 3 - Loop through the pages until done is entered.

shopping_list = {
    "Display 1": ["What would you like to add to your shopping list?"],
    "User Input 1": ["Enter Item name","or", "Enter 'done' to finish"],
    "User Input 2": ["Enter Item Quantity"],
    "Display 2": ["Your Shopping list", "Item name", "Quantity"]
}

#Step 4 - Create the display function that prints the names and numbers of pages in the prototype
# in sequential order with each page number increasing with each step.

page_number = 1
for category, items in shopping_list.items():
    print(f"\n--- Page {page_number} ---")
    print(f"Page type: {category}")
    for item in items:
        print(item)
    page_number += 1

#Step 5 - Print total pages for design.
print("\n--- total pages in design ---")
print(page_number-1)