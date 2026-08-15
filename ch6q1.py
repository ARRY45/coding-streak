a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

if a >= b and a >= c and a >= d :
    print("FIRST NUMBER IS GREATEST")

elif b >= a and b >= c and b >= c:
    print("SECOND NUMBER IS GREATEST")

elif c>=a and c >=b and c>=d:
    print("Third NUMBER IS GREATEST")

else:
    print("fourth NUMBER IS GREATEST ")