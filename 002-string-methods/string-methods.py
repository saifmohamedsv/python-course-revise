# Some methods that are built-in the <class str />.
String = "Saif 1Mohamed"

# len() method - to calculate the length of a string (how many chars).
print(len(String))  # output: 12, counts the white space.


# find() method allows you to find characters in a string.
print(String.find("a"))
# output: 1, will find the first letter will match and quit.


# capitalize() method capitalize the first letter of string
print("saif".capitalize())
# output: Saif


# upper() method capitalize the whole string.
print(String.upper())
# output: SAIF MOHAMED


# lower() method lowercase the whole string.
print(String.lower())
# output: saif mohamed


# isdigit() checks if the string is consists of numbers and just numbers.
print(String.isdigit())
# output: False
print("123".isdigit())
# output: True


# isalpha() checks if the string consists of letters and only letters, !no whitespaces!
print(String.isalpha())
# output: False
print("saif".isalpha())
# output: True
