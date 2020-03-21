def spam(number):
     return ('bulochka' * number)
print(spam(5))

def my_sum(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum
list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
print (my_sum(list_of_numbers))


def shortener(string):
    new_string=[]
    string_1=list(string.split())
    for i in string_1:
        if len (i) > 6:
            i=i[:6]+'*'
        new_string.append (i)
    res=' '.join(new_string)
    return (res)
    
string='qwertyui asdfghjkl zxcvb'
print (shortener(string))


def compare_ends(words):
    new_string=[]
    for i in words:
        if len (i) >= 2 and i[:1]==i[-1:]:
            new_string.append (i)
    return (len(new_string))
words=['adda', 'baaab', 'aby', 'gooog', 'aa', 'a']
print (compare_ends(words))
