test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print(test_dict)

value = input("Enter the value to check: ")

frequency = list(test_dict.values()).count(int(value))

print("Frequency of", value, "is:", frequency)
