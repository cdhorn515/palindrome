import re

# ask user to input string

userString = input("Please enter a word or phrase and I will tell you if it's a palindrome:  ")

# remove non alpha characters (using regex) and change case
replacedString = re.sub("[^a-zA-Z]", "", userString).lower()

reversedString = replacedString[::-1]

if replacedString == reversedString:
    print(f"{userString} is a palindrome")
else:
    print(f"{userString} isn't a palindrome")


# reverse string and assign to variable

# compare variables
