x=1
marks=61
grades=100
tequilashots=5
#if statement
if (x>=0):
    print("The number is positive")
    print(4+10)
#if..else statement
if marks>=60:
    print("You have passed")
else:
    print("You have failed")
#if ...elif...els
if grades<=29 and grades>=0:
    print("You have failed")
elif grades<=49 and grades>=30:
    print("You have passed")
elif grades<=79 and grades>=50:
    print("You have credid")
elif grades<=100 and grades>=80:
    print("You have distinction")
else:
    print("Wrong input")
if tequilashots>=5:
    print("Wewe ni tanker")
elif tequilashots<=4 and tequilashots>=2:
    print("Uko mahali")
elif tequilashots<=1 and tequilashots>=0:
    print("Mtoi")
else:
    print("DEAD")