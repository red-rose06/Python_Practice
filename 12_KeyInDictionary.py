'''Program to check whether a key already exists in a dictionary'''

d = {}

n = int(input("Enter number of key-value pairs for the dictionary: "))
for i in range (0,n):
    k = input(f"Enter key of pair{i+1}: ")
    v = input(f"Enter value of pair{i+1}: ")
    d[k]=v

print(f"Dictionary is: {d}")

find = input("Enter key to find: ")

if find in d:
    print("Key found!")
else:
    print("Key not found")