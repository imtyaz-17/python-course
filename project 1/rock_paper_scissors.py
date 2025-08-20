import random

choices = {1:'rock', 2:'paper', 3:'scissors'}

def rock_paper_scissorrs(user_choice):
    computer_choice = random.choice(list(choices.keys()))
    print(f"Computer chose: {choices[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("You lose!")


try:
    user_choice = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
    if user_choice not in choices:
        raise ValueError("Invalid choice")
    rock_paper_scissorrs(user_choice)

except ValueError:
    print("Please enter a valid number: 1, 2, or 3.")
