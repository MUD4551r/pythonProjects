def is_prime_custom(n):
    
    if n <= 1:
        return False
    
    
    i = 2
    
    
    while i * i <= n:
        if n % i == 0:
            
            return False
        i += 1
        
   
    return True


number_to_test = int(input("enter number : "))
if is_prime_custom(number_to_test):
    print(f"{number_to_test} is Prime!")
else:
    print(f"{number_to_test} is Not Prime.")
    
