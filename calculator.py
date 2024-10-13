def calc():
    print("Calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation")
    print("1. (+)")
    print("2. (-)")
    print("3. (*)")
    print("4. (/)")

    operation = input("choose one operation (1/2/3/4): ")

    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error")
    else:
        print("Invalid operation choice.")
calc()