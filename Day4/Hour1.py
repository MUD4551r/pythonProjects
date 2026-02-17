# function to greet user by name
def greet(name):
    print(f"Aslam u alakum {name} ")
greet("mudassir")

# calculate square of a number

def square(num):
    return num * num
print(square(5))

def even(num):
    if num % 2 == 0:
        print(f"{num } is even number")
    else:
        print(f"{num} is odd number")
        
even(7)

# function to check prime number
def prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
num = int(input("enter number : "))
if prime(num):
    print(f"{num} is Prime!")
else:
    print(f"{num} is Not Prime.")
    
def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is greatest")
    elif b > a and b > c:
        print(f"{b} is greatest")
    elif c > a and c > b:
        print(f"{c} is greatest")
    else:
        print(f"{a,b,c} are equal numbers")
max(1,10,4)