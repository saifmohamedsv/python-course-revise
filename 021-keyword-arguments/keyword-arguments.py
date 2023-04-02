# keyword arguments = arguments preceded by an identifier when we pass them, so the order will not matter
# unlike positional arguments, Python can know the name of each param.

def OrderMatters(name, age):
    print("Hello, " + name + " ur age is: " + age)


OrderMatters("21", "Saif")
# Output: Hello, 21 ur age is Saif (Positional Arguments)


def OrderDontMatters(name: str, age: int):
    print("Hello, " + name + " ur age is " + str(age))


OrderDontMatters(age=21, name="Saif")
# Order of the params does not matters. because we used identifiers.
