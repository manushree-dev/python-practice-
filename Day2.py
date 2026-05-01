#Find most frequent element in a list
'''list = list(map(int,input("Enter numbers:").split()))
counter = 0
final_counter = 0
final_ele = None
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            counter += 1
            element = list[i]
        if counter > final_counter:
            final_ele = element
print(final_ele)'''

#Sorting a list
'''list = list(map(int,input("Enter the list:").split()))
for i in range(len(list)):
    temp = 0
    for j in range(i+1,len(list)):
        if(list[i] > list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)'''

#Merge two sorted lists
'''list1 = list(map(int,input("Enter the list1:").split()))
list2 = list(map(int,input("Enter the list2:").split()))

for i in range(len(list2)):
    list1.append(list2[i])
print(list1)'''

#Check if two strings are anagrams
'''str1 = input("Enter the string1:").lower()
str2 = input("Enter the string2:").lower()
count = 0

if len(str1) != len(str2):
    print("Not anagrams")
else:
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
                break
        print(count)
    if count != len(str1):
        print("Not anagrams")
    else:
        print("Anagrams")'''




