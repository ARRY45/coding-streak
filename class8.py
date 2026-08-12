choice = int(input("Enter 1 for inches to centimeter\nEnter 2 for centimeters to inches"))

if choice == 1:
    inches = float(input("Enter the inches :"))
    cm = inches * 2.54
    print("centimeters = ",cm)

elif choice == 2:
    cm = float(input("Enter the centimeters :"))
    inches = cm/2.54
    print("inches = ",inches)

else:
    print("Invalid Number")