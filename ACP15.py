bill = float(input("Enter the bill amount: $"))
paid = float(input("Enter the amount paid: $"))

if bill < paid:
    change = paid - bill
    print(f"Shopkeeper should return: ${change:.2f}")
else:
    print("The amount paid is not enough to cover the bill.")