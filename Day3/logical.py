age = 20
citizen = True

if age >= 18 and citizen:
    print("eligible to vote")
    
# 1. ask age and salary check loan eligibility

age = int(input("Enter Age : "))
salary = int(input("Enter salary: "))

if age >= 25 and salary >= 50000:
    print("eligible for loan")
else:
    print("not eligible... sorry")
    
# 2. Ask username + password 

username = 'Muda'
password = "muda@1122"

uname = input("Enter Username : ")
upwd = input("Enter Password :")

if uname == username and upwd == password:
    print("=====================================")
    print("  welcome back ",username)
    print("=====================================")
else:
    print("username or password incorrect please try again.....")
    
# check if a number is between 10 and 50

num = int(input("Enter a number : "))

if num > 10 and num < 50:
    print(f"{num} lies between 10 and 50")
else :
    print(f"{num} not line between 10 and 50")