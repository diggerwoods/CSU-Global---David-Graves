# Portfolio Project
# Milestone 1: 

class ItemToPurchase:

  def __init__(self,
               item_name="none",
               item_price=0,
               item_quantity=0,               
               item_description="none"):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

  # prints out the item cost
  def print_item_cost(self):
    self.item_price = int(self.item_price)
    self.item_quantity = int(self.item_quantity)
    return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price*self.item_quantity}'

  # prints item_description attribute for an itemToPurchase object
  def print_item_description(self):
    return f'{self.item_name}: {self.item_description}'

# Milestone 2: 
# Step 4 -> Build the ShoppingCart class with specific data attributes and related methods.

class ShoppingCart:

  def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = []

  # Add method for adding items to the cart.
  def add_item(self, ItemToPurchase):
    self.cart_items.append(ItemToPurchase)

  # Add method for removing items from the cart.
  def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

  # Add method for modifying items in the cart
  def modify_item(self, ItemToPurchase):
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == ItemToPurchase.item_name:
                if ItemToPurchase.item_description != "none":
                    cart_item.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price != 0:
                    cart_item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    cart_item.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

  # Add method to return the total number of item in the cart.
  def get_num_items_in_cart(self):
    total_quantity = 0
    for x in self.cart_items:
      self.item_quantity = int(x.item_quantity)
      total_quantity += self.item_quantity
    return total_quantity

  # Add method to return the total cost of items in cart
  def get_cost_of_cart(self):
    cart_cost = 0
    for i in self.cart_items:
      self.item_price = int(i.item_price)
      self.item_quantity = int(i.item_quantity)
      cost = self.item_price * self.item_quantity
      cart_cost += cost
    return cart_cost

  # Add method to return the total of objects in cart
  def print_total(self):
    if len(self.cart_items) == 0:
      print("SHOPPING CART IS EMPTY\n")
    else:
      print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
      print(f'Number of Items: {self.get_num_items_in_cart()}\n')
      for item in self.cart_items:
        print(item.print_item_cost())
      print()
      print(f'Total: ${self.get_cost_of_cart()}')

  # Add method to output the name of the item and description
  def print_descriptions(self):
    print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
    print()
    print("Item Descriptions")
    for item in self.cart_items:
      print(item.print_item_description())

# menu
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
# implement Output shopping cart menu
def execute_menu(char, cart):
  if char == "a":
    print("ADD ITEM TO CART")
    item_name = input("Enter the item name:\n")
    item_desc = input("Enter the item description:\n")
    item_price = input("Enter the item price:\n")
    item_quantity = input("Enter the item quantity:\n")
    item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
    cart.add_item(item)
       
  elif char == "r":
    print("REMOVE ITEM FROM CART")
# code to remove will be added in Final

  elif char == "c":
    print("CHANGE ITEM QUANTITY")
# code to change will be added in Final
    
  elif char == "i":
    print("OUTPUT ITEMS' DESCRIPTIONS")
    cart.print_descriptions()
    
  elif char == "o":
    print("OUTPUT SHOPPING CART")
    cart.print_total()

if __name__ == "__main__":
  choice = ""
  options = ["a", "r", "c", "i", "o", "q"]
  # ShoppingCart parameters
  custo_name = input("Enter customer's name:\n")
  today_date = input("Enter today's date:\n")
  print()
  sc = ShoppingCart(custo_name, today_date)
  print(f'Customer name: {sc.customer_name}')
  print(f"Today's date: {sc.current_date}\n")
  print_menu()
  print()
  # this while loop prints the menu until user enters q
  while True:
    
    choice = input("Choose an option:\n")
    if choice == "q":
      break
    else:
      if choice in options:
        execute_menu(choice, sc)
        print()
        print_menu()
        print()
      else:
        choice = input("Choose an option from the menu:\n") 