for i in range(1, 21):
    print(i, end=",")
print()
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=",")
print()
n = int(input("enter table limit"))

for i in range(1, n):
    print(i*5, end="|")
print()
    
# while loop

count = 1
while count <= 10:
    print(count, end="")
    count+=1
print()
while count >= 1:
    print(count, end="")
    count-=1
print()

num = int(input("Enter number"))

count = 1

while count <= 20:
    print(num * count)
    count+=1
    
username = "Muda"
password = "Mudas@0000"



for i in range(1, 5):
    uname = input("enter username : ")
    pwd = input("Enter password : ")
    if uname == username and password == pwd:
        print("Login successful.")
        break
    else:
        print("try again ..")
   