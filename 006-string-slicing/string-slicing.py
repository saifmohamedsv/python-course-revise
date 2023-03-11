# Slicing = Creating a substring by extracting elements from other strings
# Two Ways:
# 1- Indexing [start:stop:step]
# 2- Slice Function

name = "Saif Mohamed"

# 1- Indexing Way

first_name = name[0:4]
# OR: `first_name = name[:4]` - we removed the zero here (Same Result) It knows that the start will be zero anyways
print("First Name: ", first_name)


last_name = name[5:]  # From index 5 to the end
print("Last Name: ", last_name)


stepper_name = name[0:12:2]
# The last number is (step) It will count from the start and increase by the step, 1 + 2 = 3 / 3 + 2 = 5 and so on (1, 3, 5, 7...) those will be the indices of the letters
print("Stepper Name: ", stepper_name)


reversed_name = name[::-1]
# I'm telling the string traverse yourself from the very end to the very beginning
print("Reversed Name: ", reversed_name)  # Output: demahoM fiaS


# 2- Slice Function Way
website = "https://saifmohamedsv.web.app"

# Start, Stop, Step - Just like indexing
website_slice = slice(8, len(website))  # Define a slice
# Here I sliced the ( https:// ) till the end of the string
print(website[website_slice])
