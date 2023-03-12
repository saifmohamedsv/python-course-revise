# If Statements = a block of code will execute only if it's condition is true

age = int(input("Enter your age: "))  # Collect age as integer from the user

if age >= 18:  # Check if the age is bigger than or equal 25
    # If and only if the age is more than or equal 25 the print will run
    print("You're an adult!")

elif age == 15:  # if the first condition is not true will check this one after...
    print("You're 15!")

else:  # This will be checked at the end, after all the `elif` statements
    print("You still a kid!")
