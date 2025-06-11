age = int(input("Enter your age: "))

day = str(input("Enter the day: "))

price = 12 if age >= 18 else 8

if day == "wednessday":
    price -= 2

print("Your ticket price is $",price)