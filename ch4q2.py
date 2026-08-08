marks = []

m1 = int(input("Enter first student marks :"))
marks.append(m1)

m1 = int(input("Enter second student marks :"))
marks.append(m1)

m1 = int(input("Enter third student marks :"))
marks.append(m1)

m1 = int(input("Enter fourth student marks :"))
marks.append(m1)

m1 = int(input("Enter fifth student marks :"))
marks.append(m1)

m1 = int(input("Enter sixth student marks :"))
marks.append(m1)

marks.sort()

print(sum(marks))

print(marks)
