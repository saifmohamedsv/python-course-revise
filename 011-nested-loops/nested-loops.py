# nested loops = The inner loop will finish all it's iterations before the outer loop finish one iteration

rows = int(input("How many rows: "))
columns = int(input("How many column: "))
sympol = input("Enter a sympol to use: ")


for i in range(rows):
    for j in range(columns):
        print(sympol, end="")
    print()
