String = input("Please enter a string: ")

string2 = ('')

for i in String:
    string2 = i + string2

print("\nThe Original String = ", String)
print("The Reversed String = ", string2)