amount = int(input("Enter the number : "))
a = amount
Length = 0

while a > 0:
    Length = Length + 1
    a = int(a / 10)

if Length >= 4:
    Length = int(Length / 2)
    count = 0

    while amount > 0:
        digit = amount % 10

        if count == Length:
            Between1 = digit
        elif count == (Length - 1):
            Between2 = digit

        amount = int(amount / 10)
        count = count + 1

    prod = Between1 * Between2
    print("\nProduct of Mid digits (" + str(Between1) +
          "*" + str(Between2) + ") = ", prod)

else:
    print("\nIt's not a 4 or more than 4-digit number!")
