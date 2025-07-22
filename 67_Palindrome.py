'''Program to check whether a number is palindrome or not'''

n = int(input("Enter a number: "))
s = str(n)
s2 = s[::-1]

if s==s2:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")
