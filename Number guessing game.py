import random
logo = r""" 
 .---. .-. .-..----. .----. .----.     .--.     .-. .-..-. .-..-.   .-..----. .----..----.    
/   __}| { } || {_  { {__  { {__      / {} \    |  `| || { } ||  `.'  || {}  }| {_  | {}  }   
\  {_ }| {_} || {__ .-._} }.-._} }   /  /\  \   | |\  || {_} || |\ /| || {}  }| {__ | .-. \   
 `---' `-----'`----'`----' `----'    `-'  `-'   `-' `-'`-----'`-' ` `-'`----' `----'`-' `-'   """
print(logo)


def easy(number):
    for i in range(0,10):
        print(f"you have {10-i} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess < number:
            print("TOO LOW")
            if i == 9:
                print("You've run out of guesses.Play again to win")
                print(20 * "\n")
                break
            print("Guess again.")
        elif guess > number:
            print("TOO HIGH")
            if i == 9:
                print("You've run out of guesses.Play again to win")
                print(20 * "\n")
                break
            print("Guess again.")
        else:
            print(f"You got it! The answer was {number}.")
            print(20*"\n")
            break

def hard(number):
    for i in range(0, 5):
        print(f"you have {5-i} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess < number:
            print("TOO LOW")
            if i == 4:
                print("You've run out of guesses.Play again to win")
                print(20 * "\n")
                break
            print("Guess again.")
        elif guess > number:
            print("TOO HIGH")
            if i == 4:
                print("You've run out of guesses.Play again to win")
                print(20 * "\n")
                break
            print("Guess again.")
        else:
            print(f"You got it! The answer was {number}.")
            print(20 * "\n")
            break


def play():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,101)
    choice = input("Choose a difficulty. Type 'easy' or 'hard':")
    if choice == 'easy':
        easy(number)
    elif choice == 'hard':
        hard(number)

while True:
    play()
