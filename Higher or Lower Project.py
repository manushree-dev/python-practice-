import random
from game_data import data
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)

def compare(A,B,choose):
    if A['follower_count'] > B['follower_count'] and choose == 'a' or B['follower_count'] > A['follower_count'] and choose == 'b':
        return True
    else:
        return False


game_is_true = True
counter = 0
B = random.choice(data)

while game_is_true:
    A = B
    B = random.choice(data)

    if A == B:
        B = random.choice(data)
    print(f"Compare A:{A['name']},a {A['description']} from {A['country']}.")
    print(vs)
    print(f"Against B:{B['name']},a {B['description']} from {B['country']}.")
    choose = input("Who has more followers?Type 'A' or 'B':").lower()
    result= compare(A,B,choose)

    if result == True:
        counter += 1
        print(f"You're right! Current score:{counter}")
    else:
        game_is_true = False
        print(f"Sorry, that's wrong. Final score:{counter}")





