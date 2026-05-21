import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lists = [rock,paper,scissors]
while(1):
    com = random.choice(lists)
    user = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
    print(f"You chose {lists[user]}")
    print(f"Computer chose {com}")
    if user == 0 and com == paper or user == 1 and com == scissors or user == 2 and com == rock:
        print("You lose")
        break
    elif lists[user] == com:
        print("Its draw")
    else:
        print("You won!")
