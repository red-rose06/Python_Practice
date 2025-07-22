'''Program to get substring of a string'''

s = input("Enter a string: ")
a = int(input("Enter starting index of substring: "))
b = int(input("Enter ending index of subtring: "))

sub = s[a:b+1]
print(f"Subtring of '{s}' is '{sub}'")

print("Please enter valid indices")