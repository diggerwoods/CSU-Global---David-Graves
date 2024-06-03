#Portfolio Milestone
#Step 1: Build the ItemToPurchase class

class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

#Step 2: Prompt user for two items and create two objects of the ItemToPurchase class.
print("Item 1")    
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

#Step 3: Add the costs of the two items together and output the total cost.

total_cost = item1.item_quantity * item1.item_price + item2.item_quantity * item2.item_price
print("\nTOTAL COST:")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${total_cost}")