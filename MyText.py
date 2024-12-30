def number_of_words(text):
    if text==" ":
        return 0
    else:
        no_words=1
    for char in text:
        if char==" ":
            no_words+=1
    return no_words

def list_of_words(text):
    list=[]
    j=0
    for i in range(0,len(text)):
        if text[i]==" ":
            list.append(text[j:i])
            j=i+1
    list.append(text[j:])
    return list

def lengh_sort(text):
    list=list_of_words(text)
    for i in range(0,len(list)):
        for j in range(0,len(list)-i-1):
            if len(list[j])<len(list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
    return list

def alpha_sort(text):
    list=list_of_words(text)
    for i in range(0,len(text)):
        for j in range(0,len(list)-i-1):
            if list[j].lower()>list[j+1].lower():
                list [j], list[j+1]=list[j+1], list[j]
    return list
