def reverse(s):
    d=s[::-1]
    return d
def count_vowels(s):
    a='aeoiu'
    c=0
    for i in s.lower():
        if i in a:
            c+=1
