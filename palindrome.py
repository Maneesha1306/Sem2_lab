def palindrome(string):
    rev=string[::-1]
    print("Original:",string)
    print("Reversed:",rev)
    if rev==string:
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

string=input("Enter string:")
palindrome(string)