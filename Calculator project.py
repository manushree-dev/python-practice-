from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
cal_operations = {"+":add,"-":sub,"*":mul,"/":div}

while(1):
    n1 = int(input("Whats the first number?:"))
    for key,value in cal_operations.items():
        print(key)

    while(1):
        operation = input("Pick an operation:")
        n2 = int(input("Whats the next number?:"))
        result = cal_operations[operation](n1,n2)
        print(result)

        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if decision == 'n':
            break
        elif decision == 'y':
            n1 = result
            continue






