import math

r = float(input("Enter the radius :"))
h = float(input("Enter the height :"))

cylinder = math.pi * r**2 * h 
sphere = 4/3 * math.pi * r**3
cone = 1/3 * math.pi * r**2 * h

print("Volume of cylinder = ",cylinder)
print("Volume of sphere = ",sphere)
print("Volume of cone = ",cone)