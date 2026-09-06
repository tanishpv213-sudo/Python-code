print("Shopping Total Calculator")

item = input("Item name: ")
price = float(input("Price: $"))
quantity = int(input("Quantity: "))

subtotal = price * quantity
tax = subtotal * 0.08  
total = subtotal + tax

print("\nReceipt")
print("----------------")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
