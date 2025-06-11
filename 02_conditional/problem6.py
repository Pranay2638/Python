distance = int(input("Enter the distance to be covered: "))

if distance < 3:
    print("walk")
elif 3 <= distance <= 15:
    print("Bike")
else:
    print("Car") 