#Hashing: Hash Function --->Hash Values
#       Hash Table 

def Frequency_Count(s):
    freq = {}
    for ch in s:
        if ch  not in freq :
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq
print(Frequency_Count("abcabc")) #{'a':2,'b':2,'c':2}
# Contains Dulpicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(nums) != len(set(nums))
print(containsDuplicate([1,2,3,4]))