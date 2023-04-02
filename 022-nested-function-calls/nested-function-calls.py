# Nested Fujnction Calls = function call inside another function call
# and the innermost function return's value will used as an argument for the second call

# Bad Code ‼️ ( Long Way )
num = input("Enter a number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)


# Good Code ( Shorter Way )
print(round(abs(float(input("Enter a number: ")))))
