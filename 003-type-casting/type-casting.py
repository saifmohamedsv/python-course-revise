# Type casting = convert one data type to another one Ex: string => integer

# Define x, y, z variables with three different data types
x = 1  # Whole Integer
y = 2.0  # Float
z = "3"  # String

print(x)  # 1
print(int(y))
# y was 2.0 as a float, not we used the method int() to cast it into just 2, as a whoel integer

z = int(z)  # converting "3" into integer 3

x = float(x)  # coverting 1 integer to 1.0 float

# This line👇 will generate an error cause we cannot concatenate string and numbers ❌
print("The number is" + x)

# Solved ✅
print("The number is " + str(x))  # The number is 1
