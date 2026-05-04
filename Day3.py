'''#Reverse a string without slicing
str = input("Enter a string:").lower()
my_list = list(str)
temp = ''
length = len(str)
k = int(length/2)
for i in range(k):
    temp = my_list[i]
    my_list[i] = my_list[length-i-1]
    my_list[length - i - 1] = temp

result = ''.join(my_list)
print(result)'''

'''
#Check palindrome
str = input("Enter a string:").lower()
my_list = list(str)
temp = ''
length = len(str)
k = int(length/2)
for i in range(k):
    temp = my_list[i]
    my_list[i] = my_list[length-i-1]
    my_list[length - i - 1] = temp

result = ''.join(my_list)
print(result)
if str == result:
    print("A Palindrome")
else:
    print("Not a palindrome")'''

#Count vowels and consonants in a string
'''my_str = input("Enter a string:").lower()
vowel = 0
cont = 0
for i in range(len(my_str)):
    if my_str[i] in ('a','e','i','o','u'):
        vowel += 1
    else:
        cont += 1
print(vowel,cont)'''

#Find second-largest number in a list
'''my_list = list(map(int,input("Enter the list:").split()))
f_largest = my_list[0]
smallest = my_list[0]

for i in range(len(my_list)):
    if my_list[i] > f_largest:
        f_largest = my_list[i]
    elif my_list[i] < smallest:
        smallest = my_list[i]

print(f_largest)
print(smallest)
s_largest = None
for i in range(len(my_list)):
    if my_list[i] != f_largest:
        if s_largest is None or my_list[i] > s_largest:
            s_largest = my_list[i]

print(s_largest)'''


