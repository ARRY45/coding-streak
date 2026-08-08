marks = {     
    "Arry": 100,
    "Navjot": 100,
    "Aman" : 98,
    "Rahul" : 76,
}

# print(marks.items()) #gives items 
# print(marks.keys()) #gives keys
# print(marks.values())
# marks.update({"Arry": 99,})
# print(marks)

print(marks.get("Arry")) #prints none if name is not defined 
print(marks["Arry"]) #prints error if name is not defined

