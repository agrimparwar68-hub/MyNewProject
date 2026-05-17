#count number of words in the function
def number_of_wordes():
    text = input("Enter a sentence: ")
    words = text.split()   
    return len(words)
    
count = number_of_wordes()
print("Number of words:", count)
