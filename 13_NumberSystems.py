'''Program to convert decimal to binary, hex and octal'''

def d_to_b(n):
    b = ""
    if n==0:
        return 0
    while n>0:
        b = str(n%2) + b
        n=n//2
    return b

def d_to_o(n):
    o = ""
    if n==0:
        return 0
    while n>0:
        o = str(n%8) + o
        n=n//8
    return o

def d_to_h(n):
    h_digits = "0123456789ABCDEF"
    h = ""
    if n==0:
        return 0
    while n>0:
        h = h_digits[n%16] + h
        n=n//16
    return h

num = int(input("Enter a decimal number: "))
print(f"{num} in binary is {d_to_b(num)}")
print(f"{num} in octal is {d_to_o(num)}")
print(f"{num} in hexadecimal is {d_to_h(num)}")