choice = int(input("Enter 1 for usd to inr\nEnter 2 for euro to inr"))

if choice == 1:
    usd = float(input("Enter the usd dollars :"))
    inr = usd * 92
    print("inr = ",inr)

elif choice == 2:
    euro = float(input("Enter the european dollor :"))
    inr = euro * 105
    print("inches = ",inr)

else:
    print("invalid number")