'''Input string from user. Use continue keyword to remove spaces'''

s = input("Enter a string: ")
result = ""

for c in s:
    if c == " ":
        continue
    result += c

print("String without spaces:", result)