'''Program to find mean, mode and median'''

l=[1,35,54,8,34,7,9,6,-3,87, 35, 35]

mean = sum(l)/len(l)

mode=0
c=0
c_max=0
for i in range(0,len(l)):
    j=i
    c=0
    while j<len(l):
        if l[i]==l[j]:
            c+=1
        j+=1
    if c>c_max:
        c_max = c
        mode = l[i]

median=0
l_new = sorted(l)
print("Sorted list: ",l_new)
n=len(l)-1

if n%2!=0:
    median = l_new[(n+1)//2]
else:
    median = (l_new[(n//2)-1]+l_new[n//2])/2

print(f"Mean: {mean}, Median: {median}, Mode: {mode}")