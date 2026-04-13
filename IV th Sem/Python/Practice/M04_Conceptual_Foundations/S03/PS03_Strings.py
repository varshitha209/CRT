#String ==> Immutable ==> '' or "" 
s = "python"
s= s.capitalize()
print(s)
#Reverse a String:
def Reverse_Str(s):
    res = ""
    stop = -1 * (len(s)+1)
    for i in range(-1,stop,-1):
        res = res+s[i]
    return res

print(Reverse_Str("ABC"))
def Reverse_Str(s):
    res = "" 
    for ch in s:
        res = ch +res 
    return res
print(Reverse_Str("PYTHON"))

def is_palindrome(s):
    return s == Reverse_Str(s)
    
print(is_palindrome("abc"))
print(is_palindrome("madam"))
# Check whether the given string are anagrams or not
def Frequency_Count(s):
    freq = {}
    for ch in s:
        if ch  not in freq :
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq
print(Frequency_Count("abcabc")) #{'a':2,'b':2,'c':2}

def Anagrams(s1,s2):
    return Frequency_Count(s1) == Frequency_Count(s2)
print(Anagrams("paces","space"))# True
print(Anagrams("aabbbcc","aac")) #False
from collections import Counter 

