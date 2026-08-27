try:
    number = int(input("Enter a number: "))
    print("The number intended is", number)

except ValueError as e:
    print("Except :",e)