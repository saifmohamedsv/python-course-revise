# variables is a container for a specific value, and can store variety of datatypes
first_name = "Saif"
last_name = "Mohamed"

# concatenation -- Adding two string to one
print(first_name + " " + last_name)

# The 'type' function - generate the type of this data (ex: string, number ...etc)
print(type(first_name))

year_of_birth = 2002

# Editing variable's replacing the old one anytime
year_of_birth = year_of_birth + 1
print(year_of_birth)  # output: 2003

# Boolean True or False
attractive = True
print(attractive)
print(type(attractive))

# Multiple Assignments - One line of code variables declaration

## -- Normal Way
# name = "Saif"
# age = 21
# is_human = True


# Multiple Assignment Way
name, age, is_human = "Saif", 21, True

print(name, age, is_human)
