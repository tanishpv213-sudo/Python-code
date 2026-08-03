num = int(input("Enter any number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")