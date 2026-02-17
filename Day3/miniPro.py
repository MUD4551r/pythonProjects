# Number Guessing Game
secret = 7
guess = 0


while guess != secret:
    
    guess = int(input("Guess the number : "))
    if guess > secret:
        print("Too hight")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
    