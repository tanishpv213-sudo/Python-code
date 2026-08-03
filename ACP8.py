num = int(input("Enter the number: "))
n = int(input("Enter the value of n: "))

print("Powers of", num, "are:")

for i in range(1, n + 1):
    print(f"{num}^{i} = {num ** i}")
