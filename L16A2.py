try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result is :", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Comma is missing. Please enter two numbers separated by a comma like this: 5, 2")
except:
    print("Wrong input")
else:
   print("No exception")

finally:
    print("this will always execute")