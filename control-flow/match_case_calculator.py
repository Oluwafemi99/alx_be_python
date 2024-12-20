num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        rusult = (num1 + num2)
    case "-":
        result = (num1 - num2)
    case "*":
        result = (num1 * num2)
    case "/":
        if num2 != 0:
            result = (num1 / num2)
        else:
            result = ("Error: division by zero is not allowed")
    case _:
        resutl = ("invalid")
print (f"The result is {result}")