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

class ShoppingCart(ItemToPurchase):

  def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
    ItemToPurchase.__init__(self)
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = []

  # Add method for adding items to the cart
  def add_item(self, ItemToPurchase):
    self.cart_items.append(ItemToPurchase)

  # Add method for removing items from the cart
  def remove_item(self, item_name):
    count = 0
    for i in range(len(self.cart_items) - 1):
      if self.cart_items[i].item_name == item_name:
        self.cart_items.pop(i)
        count += 1
        break
    if count == 0:
      print("Item not found in cart. Nothing removed.")

  # modify item in cart by the name
  def modify_item(self, obj):
    for cart_item in self.cart_items:
      if cart_item.item_name == obj.item_name:
        cart_item.item_quantity = obj.item_quantity
    else:
      print("Item not found in cart. Nothing modified.")

  # returns the number of item in the list
  def get_num_items_in_cart(self):
    total_quantity = 0
    for x in self.cart_items:
      self.item_quantity = int(x.item_quantity)
      total_quantity += self.item_quantity
    return total_quantity

  # returns the total cost of items
  def get_cost_of_cart(self):
    cart_cost = 0
    for i in self.cart_items:
      self.item_price = int(i.item_price)
      self.item_quantity = int(i.item_quantity)
      cost = self.item_price * self.item_quantity
      cart_cost += cost
    return cart_cost

  # outputs total objects in cart
  def print_total(self):
    if len(self.cart_items) == 0:
      print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
      print(f'Number of Items: {self.get_num_items_in_cart()}\n')
      print("SHOPPING CART IS EMPTY\n")
      print(f'Total: ${self.get_cost_of_cart()}')
    else:
      print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
      print(f'Number of Items: {self.get_num_items_in_cart()}\n')
      for item in self.cart_items:
        print(item.print_item_cost())
      print()
      print(f'Total: ${self.get_cost_of_cart()}')

  # outputs the name of the item and description
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
    
# execute menu
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
    rmv_item = input("Enter name of item to remove:\n")
    cart.remove_item(rmv_item)
    
  elif char == "c":
    print("CHANGE ITEM QUANTITY")
    item_name = input("Enter the item name:\n")
    new_qunatity = input("Enter the new quantity:\n")
    new_obj = ItemToPurchase(item_name, sc.item_price, new_qunatity,
                             sc.item_description)
    cart.modify_item(new_obj)
    
  elif char == "i":
    print("OUTPUT ITEMS' DESCRIPTIONS")
    cart.print_descriptions()
  elif char == "o":
    print("OUTPUT SHOPPING CART")
    cart.print_total()


if __name__ == "__main__":
  choice = ""
  options = ["a", "r", "c", "i", "o", "q"]
  # parameters for ShoppingCart
  custo_name = input("Enter customer's name:\n")
  today_date = input("Enter today's date:\n")
  print()
  sc = ShoppingCart(custo_name, today_date)
  print(f'Customer name: {sc.customer_name}')
  print(f"Today's date: {sc.current_date}\n")
  print_menu()
  print()
  # while loop that prints the menu until user enters q - quit
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
        choice = input("Choose an option:\n")