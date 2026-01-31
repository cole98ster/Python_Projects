password = input("Enter your password: ")

strength = 5
if len(password) < 8:
    print("Password is too short. It should be at least 8 characters long.")
    strength -= 1
elif " " in password:
    print("Password should not contain spaces.")
    strength -= 1
elif password.isalpha():
    print("Password should include at least one number or special character.")
    strength -= 1
elif password.isdigit():
    print("Password should include at least one letter or special character.")
    strength -= 1
if password.islower() or password.isupper():
    print("Password should include both uppercase and lowercase letters.")
    strength -= 1
else:
    print("Password is strong.")
print(f"Password strength: {strength}/5")