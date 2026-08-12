choice = int(input("Enter 1 for inches to feet\nEnter 2 for feet to inches"))

if choice == 1:
    inches = float(input("Enter the inches :"))
    feet = inches / 12
    print("feet = ",feet)

elif choice == 2:
    feet = float(input("Enter the feet :"))
    inches = feet * 12
    print("inches = ",inches)

else:
    print("invalid number")