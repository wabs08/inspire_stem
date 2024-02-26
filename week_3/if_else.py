age = 25
if age > 18 :
    print("you are allowed to drive")

age = 16
if age > 18 :
    print("you are allowed to drive")
else:
    print("you cant drive")


salary = 45000
if salary > 30000 and salary <50000 :
    salary = salary * 0.1 + salary
    print(salary)



home_county= "Nyeri"
if home_county == "Nyeri" or home_county == "uganda" :
   print("you get a bursary")



grade = 70
if grade < 84:
    print("you are promoted to next class")
else:
    print("you repeated the class")


 
grade = 70
if grade <= 84:
    print("you are promoted to next class")
else:
    print("you repeated the class")   


grade = 70
if grade >= 84:
    print("you win a voucher worth 5000")
elif grade >=50 and grade <=84:
    print("you win a calculator") 
else:
    print("YOU GET NOTHING!!!!")
