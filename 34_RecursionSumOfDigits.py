'''Program to find sum of digits of number using recursion'''

def sum_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_digits(n//10)

num = int(input("Enter a number: "))
if num>=0:
    print(f"The sum of digits of {num} is {sum_digits(num)}")
else:
    print(f"Please enter a positive number")