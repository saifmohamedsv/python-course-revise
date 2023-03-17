# Loop Control, break/continue/pass

#  Break: used to stop the loop entirely
#  Continue: skip to the next iteration of the loop
#  Pass: does nothing :)


# 1- Break
while True:
    name = input("Enter your name: ")
    if name != "":  # If you did not write anything, so the loop will stay ask you for name over and over
        break  # If you write anything else than empty string it will stops...


# 2- Continue
phone_number = "01206-944093"
for i in phone_number:
    if i == "-":  # Check if the dash is exist in the iteration so skip it and go to the next iteration
        continue
    # This line will print every number in the variable excepts the - (dash) it will skip it
    print(i, end="")


# 3 - Pass
for i in range(1, 21):
    if i == 13:
        pass  # Acts as a placeholder
    else:
        print(i)
