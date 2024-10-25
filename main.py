#Update in the future to take an argument from command line, or from a menu selection
book="./books/frankenstein.txt"

# Function to count the words in a given book or text. Words are sets of characters between whitespace
def wordCount(bkData):
    words=bkData.split()
    return(len(words))

# Function to count the number of alphabetic characters in a given book or text
def charCount(bkData):
    alpha={}
    for i in bkData:
        if i.isalpha():
            x=i.lower()
            if x in alpha.keys():
                alpha[x]+=1
            else:
                alpha[x]=1
    
    return(alpha)
#In the future, wrap the report below into a function
with open(book,"r") as f:
    data=f.read()
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{ wordCount(data) } words found in the document")
    print(f"\n")
    chars=charCount(data)
    d=sorted(chars,key=chars.get, reverse=True)
    for key in d:
        print(f"The '{key}' character was found {chars[key]} times")

    print(f"--- End report ---")

