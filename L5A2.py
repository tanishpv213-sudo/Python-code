Net_Cost = float(input("Enter the net cost: "))
Sale_Amount = float(input("Enter the amount of sale: "))

if Sale_Amount > Net_Cost:
    Profit = Sale_Amount - Net_Cost
    print("The sale amount is greater than the net cost.")
    print(f"Profit: ${Profit:.2f}")

else:
    
    print("The sale amount is less than the net cost.")
    
