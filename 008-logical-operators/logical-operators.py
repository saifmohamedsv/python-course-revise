# Logical Operators ( AND, OR, NOT) = used to check if two or more statements are true


# Take tempreature integer from the user...
temp = int(input("What is the tempreature out there: "))

# AND
# Check if tempreature is between 0 to 25 by using the AND operator written as `and`, when using it the two conditions should be true and one of them
if temp >= 0 and temp <= 25:
    print("It's Good, you can go")
# OR
# Check either temp is more than 30 or smaller than 0, just one condition should be true to work
elif temp < 0 or temp > 30:
    print("It's Bad, you cannot go")


name = input("What is your name: ")
# NOT operator: It flips the condition from true to false and vice versa
if not name == "Saif":  # Here I'm checking if the name is not Saif, when you write anything else the condition will be True
    print("Your name is not saif")
