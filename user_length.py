# print length of given user name and print number of vowels
def user_name():
    name = input("Enter your name:- ")
    print("Length of name:", len(name))
    
    vowels = "aeiouAEIOU"
    count = 0
    for ch in name:
        if ch in vowels:
            count += 1
    
    print("Number of vowels:", count)

user_name()