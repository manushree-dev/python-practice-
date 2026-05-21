import random
'''rand_num = random.randint(1,10)
print(rand_num)'''

'''rand_num_0_to_1 = random.random() * 5 #wont include 1
print(rand_num_0_to_1)'''

'''random_float = random.uniform(1,10)
print(random_float)'''

Heads_or_Tails = random.randint(0,1)
if Heads_or_Tails == 0:
    print("Tail")
elif Heads_or_Tails == 1:
    print("Head")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
g = random.choice(friends)
print(g)
'''num = random.randint(0,len(friends)-1)
print(friends[num])'''
