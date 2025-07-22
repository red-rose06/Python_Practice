'''Program to generate random numbers between 1-20 and append them to a list'''

import random

l = []
n=1
num=0

print("Welcome to the random number generator!")

while(n!=0):
    num = random.randint(1,20)
    l.append(num)
    print(f"The updated list is: {l}")
    n=int(input("Enter 0 to exit. Enter any other number to continue: "))