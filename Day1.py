#Find duplicates in a list
#Sort dictionary by value
#Read and write a file
#Find most frequent element in list
#Merge two sorted lists
#Check if two strings ar anagrams

#Find duplicates in a list
new_list = list(map(int,input("Enter numbers:").split()))
print(new_list)
modified = []
for i in range(len(new_list)):
    if new_list[i] not in modified:
        modified.append(new_list[i])
print(modified)

'''#Sort dictionary by value
d = {}
n = int(input("Enter number of elements:"))

for i in range(n):
    key = input("Enter Key:")
    value = input("Enter value:")
    d[key] = value
print(d)

sorted_dict = dict(sorted(d.items(),key=lambda item:item[1]))
print(sorted_dict)'''

'''#Read and write a file
data = open("File.txt","r").read()
print(data)
data1 = open("File.txt","w").write(input())
data2 = open("File.txt","r").read()
print(data2)'''

