medical_cause = input("Did you have a medical cause for your absence? (Y/N): ")

if medical_cause == 'Y' or medical_cause == 'y':
    print("You are allowed")
else:
    atten = int(input("Enter your attendance percentage: "))
    if atten >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")