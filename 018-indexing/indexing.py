# Index operator = gives access to sequence's element, ( str, list, tuples s)

name = "Saif Mohamed!"
print(name[0])  # 'S'


if name[0].islower():
    name.capitalize()
    print("First letter is lowercase")
else:
    print("First letter is uppercase")

# Creating a substring
first_name = name[0: 4].upper()
print(first_name)  # SAIF

last_name = name[5:].lower()
print(last_name)  # mohamed

last_character = name[-1]
print(last_character)
