p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter your comment :")

if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("WARNING! THIS IS A SPAM COMMENT DONT CLICK ANY LINKS")

else:
    print("THIS IS NOT A SPAM MSG")