subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))
subject5 = int(input("Enter marks for subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks / 5

print("The total marks obtained is:", total_marks)
print("The percentage marks obtained is:", (total_marks / 500) * 100)