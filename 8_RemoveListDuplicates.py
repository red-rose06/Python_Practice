'''Program to remove duplicates from a list'''

l = []

lim = int(input("Enter number of elements: "))

for i in range(0,lim):
    x = input(f"Enter the element {i+1}: ")
    l.append(x)

print(f"List: {l}")

#Removing duplicates
s = set(l)
print(f"Set: {s}")

l_new = list(s)
print(f"New list without duplicates: {l_new}")