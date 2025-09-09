age = int(input("please enter the age:"))

if age<1:
    print("invalid number")
if 1<=age<=10:
    print("baby")
if 10<age<=20:
    print("teen")
if 20<age<=30:
    print("young")
else:
    print("old")
