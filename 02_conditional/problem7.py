password = str(input("Enter your password: "))

if len(password) < 6:
    print("Weak")
elif 6 <= len(password) <= 10:
    print("Medium")
else:
    print("Strong")