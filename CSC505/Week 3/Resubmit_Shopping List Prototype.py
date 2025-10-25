# Shopping list prototype in action based off "MobileAppUML" and
#  following "Page structure script"
#Step 1 - Define the function 'create_shopping_list' and dictionary 'shopping_items' 
# to store item names and quantities. 

def create_shopping_list():

    shopping_items = {} 

#Step 2 - Print Display question with if then statement attached to user input.
#Step 3 - Add 'break' if "done" is keyed and print final output.
#Step 4 - If other value keyed, ask for quantity as an integer.
#Step 5 - Create exception and re-entry for non numeric entry.
#Step 6 - On valid qty entry, loop back to initial display question until break.
    
    print("What would you like to add to your shopping list?")
    while True:
        item_name = input("Enter item name (or 'done' to display)")
        if item_name.lower() == "done":
            break
        
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        
        shopping_items[item_name] = quantity

#Step 7 - On break return "Your shopping list:" and list values with paired quantities
#  captured from previous user input.

    print("\nYour shopping list:")
    for item, quantity in shopping_items.items():
        print(f"{item}: {quantity}")

if __name__ == "__main__":
    create_shopping_list()