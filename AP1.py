a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

biggest = a
if b > biggest:
    biggest = b
if c > biggest:
    biggest = c

smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print("Biggest:", biggest)
print("Smallest:", smallest)
