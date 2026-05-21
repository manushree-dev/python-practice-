S = 15
M = 20
L = 25
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == 'Y':
    if size == 'S':
        if pepperoni == 'Y':
            S += 3
            print(f"Your final bill is: ${S}.")
        else:
            S += 1
            print(f"Your final bill is: ${S}.")

    elif size == 'M' or size == 'L':
        if size == 'M':
            if pepperoni == 'Y':
                M += 4
                print(f"Your final bill is: ${M}.")
            else:
                M += 1
                print(f"Your final bill is: ${M}.")
        elif size == 'L':
            if pepperoni == 'Y':
                L += 4
                print(f"Your final bill is: ${L}.")
            else:
                L += 1
                print(f"Your final bill is: ${L}.")
else:
    if size == 'S':
        if pepperoni == 'Y':
            S += 2
            print(f"Your final bill is: ${S}.")
        else:
            print(f"Your final bill is: ${S}.")
    elif size == 'M' or size == 'L':
        if size == 'M':
            if pepperoni == 'Y':
                M += 3
                print(f"Your final bill is: ${M}.")
            else:
                print(f"Your final bill is: ${M}.")
        elif size == 'L':
            if pepperoni == 'Y':
                L += 3
                print(f"Your final bill is: ${L}.")
            else:
                print(f"Your final bill is: ${L}.")






