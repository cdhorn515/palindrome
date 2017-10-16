import re


def main():

    user_string = input("Please enter a word or phrase and I will tell you if it's a palindrome:  ")

    replaced_string = re.sub("[^a-zA-Z]", "", user_string).lower()

    reversed_string = replaced_string[::-1]

    if replaced_string == reversed_string:
        print(f"{user_string} is a palindrome")
    else:
        print(f"{user_string} isn't a palindrome")

if __name__ == '__main__':
    main()
