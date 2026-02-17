def table (num):
    for i in range(1, 21):
        print(f"{num} X {i} = {num * i}")
num = int(input("enter number : "))
table(num)

# function to reverse a number

def reverse(number):
    idx = len(number) - 1
    while idx >= 0:
        print(number[idx], end="")
        idx = idx - 1
number = input("Enter a number to reverse : ")
reverse(number)