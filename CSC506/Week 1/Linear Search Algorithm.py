def linear_search(data, target):
   # This program performs a linear search on a list of data to find the index of the target value.
        # data: The list of items to search through.
        # target: The value to search for.
    # Returns:
        # The index of the target value in the list if found, otherwise -1.
 
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1 

# Example case 1 - Item in list
marketplace_items = ["Socks", "Shoes", "Shirts", "Hats", "Jackets", "Belts"]
search_item = "Hats"

index = linear_search(marketplace_items, search_item)

if index != -1:
    print(f"Item '{search_item}' found at index {index}")
else:
    print(f"Item '{search_item}' not found in the marketplace")

# Example case 2 - Item not in list
search_item = "Sweaters"

index = linear_search(marketplace_items, search_item)

if index != -1:
    print(f"Item '{search_item}' found at index {index}")
else:
    print(f"Item '{search_item}' not found in the marketplace")