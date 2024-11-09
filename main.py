#this is my calculator that I am building. I have no idea what Im doing 


operation = input("Enter a operation * / + -:")
num1 = float(input("what is your first number: "))
num2 = float(input("what is your second number: "))

if operation == "*":
     result = num1 * num2
     print(round(result,3))
elif operation == "/":
     result == num1/num2
     print(round(result,3))
elif operation == "+":
     result = num1 + num2
     print(round(result,3))
elif operation == "-":
     result = num1-num2
     print(round(result,2))
     
else:
     print(f"{operation} is not a valid operator")
     
     