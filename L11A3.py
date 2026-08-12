
rows = int(input("enter the number of rows: "))

halfRows = rows // 2

if rows % 2 != 0:
    halfRows += 1

spaces = halfRows - 1

for x in range(1, halfRows + 1):
    print(" " * spaces, end="")

    amount = 1
    for y in range(2 * x - 1):
        print(amount, end="")
        amount += 1

    print()
    spaces -= 1

spaces = 1

for x in range(halfRows - 1, 0, -1):
    print(" " * spaces, end="")

    amount = 1
    for y in range(2 * x - 1):
        print(amount, end="")
        amount += 1

    print()
    spaces += 1

