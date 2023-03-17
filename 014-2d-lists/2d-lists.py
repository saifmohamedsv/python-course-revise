# 2d lists = a list of lists

drinks = ["cola", "pepsi"]
dessert = ["chocolate", "chips"]

# Adding 2 lists in 1 list
food = [drinks, dessert]

print(food)
# [
#   ["cola", "pepsi"],
#   ["chocolate", "chips"]
# ]

print(food[0])  # First list which is drinks
print(food[0][0])  # First items of the first list which is drinks -> cola
# You got the idea ?! 🥲
