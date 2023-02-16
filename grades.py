grade=float(input("Enter your grade :"))
if grade >=80:
    print("you got an A")
elif grade<=79 and grade>=75:
    print("You have an A-")
elif grade<=69 and grade>=65:
    print("You have a B+")
elif grade<=64 and grade>=60:
    print("You have a B")
elif grade<=59 and grade>=55:
    print("you have a B-")
elif grade<=54 and grade>=50:
    print("You have a C+")
elif grade<=49 and grade>=45:
    print("You have a C")
elif grade<=44 and grade>=40:
    print("You have a C-")
elif grade<=39 and grade>=35:
    print("You have a D+")
elif grade<=34 and grade>=30:
    print("You have a D")
elif grade<=29 and grade>=25:
    print("You have a D-")
elif grade <=24 and grade>=1:
    print("you have an E")
else:
    print("You have an F")