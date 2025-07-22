'''Program to remove duplicates from a list'''
#Method 2

l = []

lim = int(input("Enter number of elements: "))

for i in range(0,lim):
    x = input(f"Enter the element {i+1}: ")
    l.append(x)

print(f"List: {l}")

l_new = []

for x in l:
    if x not in l_new:
        l_new.append(x)

print(f"New list without duplicates: {l_new}")