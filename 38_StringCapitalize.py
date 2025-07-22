'''Program to capitalize first letter of a string'''

s = input("Enter a string: ")
l = list(s)

if ord(l[0])>97 or ord(l[0])<122:
    l[0]=chr(ord(l[0])-32)

s_new = "".join(l)

print("Capitalized string is: ",s_new)