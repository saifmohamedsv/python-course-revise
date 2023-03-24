# Dictionary = Changable, unordered collection of unique key:value pairs
# ex: { name: "Saif", age: 21 }

capitals = {'USA': 'DC', 'EGY': 'Cairo'}

# Access Values in dictionaries
if 1:
    print("123")

print(capitals["USA"])  # If the key was not there, an error will thrown

# Get method
# If the key was not there, It will return "None"
print(capitals.get("USA"))  # DC
print(capitals.get("Russia"))  # None


# Keys Method
print(capitals.keys())  # Prints All the keys of a specific dictionary

# Values Method
print(capitals.values())  # Prints All the Values of a specific dictionary

# Items Method
print(capitals.items())  # Prints All the key & values of a dict.

# Update Method - used to add new values and update existing one
capitals.update({"Germany": "Berlin"})
capitals.update({"EGY": "Alexandria"})
print(capitals)

# Pop Method - Remove a speicific value by it's key
capitals.pop("EGY")
print(capitals)

# Clear Method - Clear all the values in a dict.
capitals.clear()
