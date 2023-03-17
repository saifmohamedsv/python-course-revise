# List = used to store multiple items in a signle variables


food = ["pizza", "burger", "rice"]

# We can access values inside that list, by mentioning the index of the item starting with 0...
print(food[0], ", the first element")
# Output: pizza

# -- Adding an item to a list
food.append("meat")
print(food, ", adding meat")
# Now the food list is ["pizza", "burger", "rice", "meat"]

# -- Remove an item from a list
food.remove("meat")
print(food, ", removing meat")
# Now the food list is ["pizza", "burger", "rice"] again

# Removing the last element of a list
food.pop()
# Now the food list is ["pizza", "burger"]


# Inserting element at a specific index of the list
food.insert(0, "cake")
# Now the food list is ["cake", "pizza", "burger"]


# Sort a list alphabetically
food.sort()

# Clear a list
food.clear()

# Print all items in a list using for loops
for item in food:
    print(item, "--list item")
