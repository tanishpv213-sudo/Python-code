rows = int(input("Enter the number of rows: "))

spaces = rows - 1

for x in range(1, rows + 1):
    print(" " * spaces, end="")

    amount = 1
    for y in range(x):
        print(amount, end="")
        amount += 1

    print()
    spaces -= 1
