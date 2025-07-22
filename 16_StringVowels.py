"""Program that counts number of vowels in a string"""

def vowel_count(s):
    v = "aeiouAEIOU"
    c=0
    for i in range(0,len(s)):
        if s[i] in v:
            c+=1
    return c

str = input("Enter a string: ")
print(f"Number of vowels in {str} is {vowel_count(str)}")