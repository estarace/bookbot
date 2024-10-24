book="./books/frankenstein.txt"


def wordCount(bkData):
    words=bkData.split()
    return(len(words))

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

