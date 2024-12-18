def count_case(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print("No. of uppercase letters:",upper)
    print("No. of lowercase letters:",lower)
    
string=input("Enter string:")
count_case(string)