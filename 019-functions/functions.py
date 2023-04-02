# Function = a block of code executed only when it get called

# We can pass pieces of data to the function
def hello(name):
    print("Hello, " + name)


hello("Saif")


# Even in shape of variables
my_name = "Saif Mohamed"
hello(my_name)


# Functions with more than one parameter...
def helloWithTwoParams(name, age):
    print(name + " is " + str(age))


helloWithTwoParams("Saif", 21)
