print("Simple Calculator")
print("Please choose a mode: 'calculate' for arithmetic operations or 'convert' for unit conversions.")
mode = input("Choose mode (calculate/convert): ").strip().lower()


if mode == 'calculate':
    x1 = input("Enter first number: ")
    operator = input("Enter operator (+, -, *, /, %): ")
    x2 = input("Enter second number: ")
    try:    
        num1 = float(x1)
        num2 = float(x2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '%':
            result = num1 % num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                exit()
        else:
            print("Error: Invalid operator.")
            exit()
            
        print(f"The result of {num1} {operator} {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
        exit()
        

elif mode == 'convert':
    value = input("Enter the just the value to convert: ")
    from_unit = input("Convert from (cm/m/km/in/ft/yd/mi): ").strip().lower()
    to_unit = input("Convert to (cm/m/km/in/ft/yd/mi): ").strip().lower()
    
    try:
        val = float(value)
        
        # Conversion factors to meters
        to_meters = {
            'cm': 0.01,
            'm': 1,
            'km': 1000,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }
        
        if from_unit in to_meters and to_unit in to_meters:
            meters = val * to_meters[from_unit]
            converted_value = meters / to_meters[to_unit]
            print(f"{val} {from_unit} is equal to {converted_value} {to_unit}.")
        else:
            print("Error: Invalid units for conversion.")
            exit()
    except ValueError:
        print("Error: Please enter a valid number for conversion.")
        exit()