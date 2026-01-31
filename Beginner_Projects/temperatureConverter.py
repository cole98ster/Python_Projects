print("Temperature Converter")
temp = float(input("Enter temperature: "))
unit = input("Is this in Celsius, Fahrenheit or Kelvin? (C/F/K): ").strip().upper()
convertedto = input("Convert to which unit? (C/F/K): ").strip().upper()

if unit == "C":
    if convertedto == "F":
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is {converted_temp}°F")
    elif convertedto == "K":
        converted_temp = temp + 273.15
        print(f"{temp}°C is {converted_temp}K")
    else:
        print("Invalid conversion unit.")
elif unit == "F":   
    if convertedto == "C":
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is {converted_temp}°C")
    elif convertedto == "K":
        converted_temp = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F is {converted_temp}K")
    else:
        print("Invalid conversion unit.")
elif unit == "K":
    if convertedto == "C":
        converted_temp = temp - 273.15
        print(f"{temp}K is {converted_temp}°C")
    elif convertedto == "F":
        converted_temp = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K is {converted_temp}°F")
    else:
        print("Invalid conversion unit.")
