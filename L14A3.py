def factorial(x):
    ''' this is a recursive function to find the factorial of an integer '''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print("the factorial of 5 is: ", factorial(5))
print("the factorial of 6 is: ", factorial(6))
print("the factorial of 9 is: ", factorial(9))
print("the factorial of 13 is: ", factorial(13))
