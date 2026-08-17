n = int(input("Enter your number :"))

product = 1

for i in range (1,n+1):
    product = product * i

print(f"THE FACTORIAL OF {n} = {product}")