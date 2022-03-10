
uName = input("what's you name ?")
yContry = input("what's your contry ?")
cName = "course python"
cPrice = 100

isstudent = input("are you student ?")


if yContry == "usa" or "germani" or "ispan":

    print(f"hello { uName} Because your from { yContry}")
    print(f"the course \"{cName}\" prise is : ${cPrice -60}")
    if  isstudent == "yes" :
        print(f"hello { uName} Because your from { yContry} and student")
        print(f"the course \"{cName}\" prise is : ${cPrice -90}")
    else:    
        print(f"hello { uName} Because your from { yContry}")
        print(f"the course \"{cName}\" prise is : ${cPrice -80}")

elif yContry == "uk" or "italy":
    print(f"hello { uName} Because your from { yContry}")
    print(f"the course \"{cName}\" prise is : ${cPrice -10}")
else:

    print(f"hello { uName} Because your from { yContry}")
    print(f"the course \"{cName}\" prise is : ${cPrice -20}")


moverate = 18
age = int(input("what's your age ?"))
if age < moverate:
    print("movie is not 4u")
else :
    print("the movie is 4u good and happy for watching ")


print("movie s not 4u "if age < moverate else "the movi s 4u good and happy for watching " )