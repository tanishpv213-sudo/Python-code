Amount = int(input("Please enter the amount for withdrawal"))

note1 = Amount // 2000
note2 = (Amount % 2000) // 500
note3 = ((Amount % 2000) % 500) // 100

print("The number of 2000 rupee note is:", note1)
print("The number of 500 rupee note is:", note2)
print("The number of 100 rupee note is:", note3)
