import random

num = random.randint(1, 100)
guesses = 0
numb = -1

while numb != num:
    numb = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    
    if numb < num:
        print("Higher number please")
    elif numb > num:
        print("Lower number please")
    else:
        print("You guessed it right! The number is", num)

print("You guessed it in", guesses, "attempts")
