num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ").strip().lower()

match op:
    case "+":
        x = num1 + num2
    case "-":
        x = num1 - num2
    case "*":
        x = num1 * num2
    case "/":
        if num2 == 0: 
            print("Cannot divide by zero.")
            exit()
        else: x = num1/num2
    case _:
        print("Invalid operand")
    
print(f"The result is {x}")