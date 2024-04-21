#1451. Rearrange Words in a Sentence
def arrangeWords(text):
    text=list(text.split())
    lst=[]
    c=0
    for i in sorted(text,key=len):
        if c==0:
            lst.append(i.title())
            c+=1
        else:
            lst.append(i.lower())
    return " ".join(lst)
