stuName = input("What is your name? ")
Math = int(input(" Enter your Math result? "))
Physcis = int(input("Enter your Physics result? "))
Biology = int(input("Enter your Biology result? "))
English = int(input("Enter your English result? "))
Chemistry = int(input("Enter your Chemistry result?? "))

avg = (Math + Physcis + Biology + English + Chemistry) / 5

if avg >= 90 and avg <= 100:
    print ("Hey " + stuName+ " your Grade is A")
elif avg >= 80 and avg <= 89:
    print ("Hey " + stuName+ " your Grade is B")
elif avg >= 70 and avg <= 79:
    print ("Hey " + stuName+ " your Grade is C")
elif avg >= 60 and avg <= 69:
    print ("Hey " + stuName+ " your Grade is D")
else:
    print ("Hey" + stuName+ " your Grade is E")