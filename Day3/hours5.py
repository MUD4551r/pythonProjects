# def is_prime_custom(n):
    
#     if n <= 1:
#         return False
    
    
#     i = 2
    
    
#     while i * i <= n:
#         if n % i == 0:
            
#             return False
#         i += 1
        
   
#     return True


# number_to_test = int(input("enter number : "))
# if is_prime_custom(number_to_test):
#     print(f"{number_to_test} is Prime!")
# else:
#     print(f"{number_to_test} is Not Prime.")
    
# # sum numbers from 1 to N
# n = int(input("Enter number : "))
# count = 0
# for i in range(1, n+1):
#     count = i + count
# print(count)

# num = "123"
# i = 2
# while i>=0:
#     print(num[i], end="")
#     i = i - 1
# print()

num = int(input("Enter a number : "))

count = 0

while num != 0:
    num = num // 10 #remove last digit
    count+=1
print("number of digits : ", count)