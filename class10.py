choice = int(input("Enter 1 for celcius to Fahrenheit\nEnter 2 for Fahrenheit to celcius"))

if choice == 1:
    celcius = float(input("Enter the celcius :"))
    fehrenheit = (celcius * 9/5) + 32
    print("fehrenheit = ",fehrenheit)

elif choice == 2:
    fehrenheit = float(input("Enter the feet :"))
    celcius = (fehrenheit - 32) * 5/9
    print("celcius = ",celcius)

else:
    print("invalid number")