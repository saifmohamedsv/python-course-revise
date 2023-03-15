import time

# for loop = a statement thast will execute block of code
#            limited amount of times
#            while loop = unlimited
#            for loop = limited


# Let's write a for loop that counts from 1 to 10
for i in range(10):
    print(i + 1)
# i, will start from 0 to 9, so to fix this we will add 1 to i each time, so we can count from 1 to 10


# This for loop took, the starting point and end point, 50, 101 - to count from 50 to 100
for j in range(50, 100 + 1):
    print(j)


# This for loop will take third argument: ( the step ) acting like a ( i + step ) every time...
for k in range(50, 101, 2):
    print(k)
# will count from 52, 54, 56 and so on...


# Strings: for loop for strings
for letter in "Saif":
    print(letter)
    # Will print each letter of the word 'Saif'

# Count down with a message, we used the 'time' module here.
#   to use the sleep method which will wait 1 second after every single line
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year !")
