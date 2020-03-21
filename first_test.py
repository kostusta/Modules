def spam(number):
     return ('bulochka' * number)

def my_sum(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum

def shortener(string):
    new_string=[]
    string_1=list(string.split())
    for i in string_1:
        if len (i) > 6:
            i=i[:6]+'*'
        new_string.append (i)
    res=' '.join(new_string)
    return (res)
    
def compare_ends(words):
    new_string=[]
    for i in words:
        if len (i) >= 2 and i[:1]==i[-1:]:
            new_string.append (i)
    return (len(new_string))