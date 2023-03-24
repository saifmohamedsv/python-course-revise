# Set = collection of value whic is unordered, unindexed and has no duplicate value

utensils = {"fork", "spoon", "knife"}
table_items = {"knife", "dish", "spoon"}

for x in utensils:
    print(x, "--item")  # - Will print the values in a different order every time


duplicated_values = {"Saif", "Saif", "Saif"}

for y in duplicated_values:
    # - Will print just one "Saif", because it is not allowed to use duplicate values in sets
    print(y, "--item")


# - We can add/remove and clear values from sets like lists
# utensils.add("kettle")
# print(utensils, "add kettle")

# utensils.remove("spoon")
# print(utensils, "remove spoon")


# - Update a set with another set
# new_set = {"new_value"}
# utensils.update(new_set)
# print(utensils, "add new set")


# - Compare values to see what a set have, but the other one does not have
print(utensils.difference(table_items))
# - Output: { "kettle", "fork", "new_value" }


# - Get the values that are common between two sets
print(utensils.intersection(table_items))
# - Output: { "kettle", "fork", "new_value" }
