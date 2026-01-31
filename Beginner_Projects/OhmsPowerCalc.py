print("Welcome to the Ohm's Law and Power Calculator!")
print("Would you like to calculate Voltage (V), Current (I), Resistance (R), or Power (P)?")
choice = input("Enter V, I, R, or P: ").strip().upper()
if choice == "V":
    try:
        I = input("Enter the current (I) in amperes (can be k, m, M or u): ").strip()
        if I == '': I = 0
        elif I.endswith('k'):
            I = float(I.replace('k','')) * 1e3
        elif I.endswith('M'):
            I = float(I.replace('M','')) * 1e6
        elif I.endswith('m'):
            I = float(I.replace('m','')) * 1e-3
        elif I.endswith('u'):
            I = float(I.replace('u','')) * 1e-6
        
        R = input("Enter the resistance (R) in ohms: ").strip()
        if R == '': R = 0
        elif R.endswith('k'):
            R = float(R.replace('k','')) * 1e3
        elif R.endswith('M'):
            R = float(R.replace('M','')) * 1e6
        elif R.endswith('m'):
            R = float(R.replace('m','')) * 1e-3
        elif R.endswith('u'):
            R = float(R.replace('u','')) * 1e-6
        
        V = round(I * R, 5)
        print(f"The voltage (V) is: {V} volts")
    except ValueError:
        print("Invalid input. Please enter numeric values for current and resistance.")
elif choice == "I":
    try:
        V = input("Enter the voltage (V) in volts: ").strip()
        if V == '': V = 0
        elif V.endswith('k'):
            V = float(V.replace('k','')) * 1e3
        elif V.endswith('M'):
            V = float(V.replace('M','')) * 1e6
        elif V.endswith('m'):
            V = float(V.replace('m','')) * 1e-3
        elif V.endswith('u'):
            V = float(V.replace('u','')) * 1e-6
        
        R = input("Enter the resistance (R) in ohms: ").strip()
        if R == '': R = 0
        elif R.endswith('k'):
            R = float(R.replace('k','')) * 1e3
        elif R.endswith('M'):
            R = float(R.replace('M','')) * 1e6
        elif R.endswith('m'):
            R = float(R.replace('m','')) * 1e-3
        elif R.endswith('u'):
            R = float(R.replace('u','')) * 1e-6
        
        I = round(V / R, 5) if R != 0 else 0
        print(f"The current (I) is: {I} amperes")
    except ValueError:
        print("Invalid input. Please enter numeric values for voltage and resistance.")
        
elif choice == "R":
    try:
        V = input("Enter the voltage (V) in volts: ").strip()
        if V == '': V = 0
        elif V.endswith('k'):
            V = float(V.replace('k','')) * 1e3
        elif V.endswith('M'):
            V = float(V.replace('M','')) * 1e6
        elif V.endswith('m'):
            V = float(V.replace('m','')) * 1e-3
        elif V.endswith('u'):
            V = float(V.replace('u','')) * 1e-6
        
        I = input("Enter the current (I) in amperes: ").strip()
        if I == '': I = 0
        elif I.endswith('k'):
            I = float(I.replace('k','')) * 1e3
        elif I.endswith('M'):
            I = float(I.replace('M','')) * 1e6
        elif I.endswith('m'):
            I = float(I.replace('m','')) * 1e-3
        elif I.endswith('u'):
            I = float(I.replace('u','')) * 1e-6
        
        R = round(V / I, 5) if I != 0 else 0
        print(f"The resistance (R) is: {R} ohms")
    except ValueError:
        print("Invalid input. Please enter numeric values for voltage and current.")
        
elif choice == "P":
    try:
        
        V = input("Enter the voltage (V) in volts: ").strip()
        if V == '': V = 0
        elif V.endswith('k'):
            V = float(V.replace('k','')) * 1e3
        elif V.endswith('M'):
            V = float(V.replace('M','')) * 1e6
        elif V.endswith('m'):
            V = float(V.replace('m','')) * 1e-3
        elif V.endswith('u'):
            V = float(V.replace('u','')) * 1e-6
        
        I = input("Enter the current (I) in amperes: ").strip()
        if I == '': I = 0
        elif I.endswith('k'):
            I = float(I.replace('k','')) * 1e3
        elif I.endswith('M'):
            I = float(I.replace('M','')) * 1e6
        elif I.endswith('m'):
            I = float(I.replace('m','')) * 1e-3
        elif I.endswith('u'):
            I = float(I.replace('u','')) * 1e-6
        
        P = round(V * I, 5)
        print(f"The power (P) is: {P} watts")
    except ValueError:
        print("Invalid input. Please enter numeric values for voltage and current.")