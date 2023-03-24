# Tuple = collection of data, ordered and un-changable

student = ("Saif", 21, "male")

# Check how many times a specific value was repeated
print(student.count("Saif"))  # Output: 1

# Get the index of specific value, like lists we start counting from 0...
print(student.index("male"))  # Output: 2


for x in student:
    print(x)


if "Saif" in student:
    print("Saif is here")
