marks1 = int(input("ENTER MARKS FOR MATHS :"))
marks2 = int(input("ENTER MARKS FOR SCIENCE :"))
marks3 = int(input("ENTER MARKS FOR ENGLISH :"))

total_percentage = (100 * (marks1 + marks2 +marks3))/300

if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed :",total_percentage)

else:
    print("You are failed dumbfuck",total_percentage)