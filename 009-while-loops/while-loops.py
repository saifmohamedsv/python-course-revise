# While loop: is a statement that will keep executing a block of code over and over while the statement is true

# while 1 == 1:
#     print("while loop is running...")


name = ""

# You will be stuck on the loop till you write any name that length > 0
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello, " + name)
