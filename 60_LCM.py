'''Program to find LCM'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max = a if a>b else b
min = b if a>b else a
f=1
check = max
lcm = 0
i=2

while f==1:
    if check%min==0:
        lcm = check
        f=0
        break
    else:
        check=max*i
        i+=1

print(f"LCM of {a} and {b} is {lcm}")