'''Program to concatenate two dictionaries in a new one'''

d1 = {}
d2 = {}
d3 = {}

n1 = int(input("Enter number of key-value pairs for the first dictionary: "))
for i in range (0,n1):
    k = input(f"Enter key of pair{i+1}: ")
    v = input(f"Enter value of pair{i+1}: ")
    d1[k]=v

n2 = int(input("Enter number of key-value pairs for the second dictionary: "))
for i in range (0,n2):
    k = input(f"Enter key of pair{i+1}: ")
    v = input(f"Enter value of pair{i+1}: ")
    d2[k]=v

d3 = d1.copy()
d3.update(d2)

print(f"First dictionary is: {d1}")
print(f"Second dictionary is: {d2}")
print(f"Concatenated dictionary is: {d3}")
