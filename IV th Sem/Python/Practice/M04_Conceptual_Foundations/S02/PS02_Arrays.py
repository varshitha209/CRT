'''
Arrays:
1) Reverse Array:
Using'''
#def ReverseArray(li):
'''solution-1
    res = []
    stop = -1*(len(li)+1)
    for i in range(-1,stop,-1):
        res.append(li[i])
    return res
    Solution-2
    stop = -1 *(len(li)+1)
    res = [li[i] for i in range(-1,stop,-1)]
    return res 
    res=[]
    n = len(li)
    for i in range(0,n//2):
        li[i],li[n-1-i] = li[n-1-i],li[i]
    return li
print(ReverseArray([1,2,3,4]))'''
'''
def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] >nums[i+1]:
            return False
    return True
print(is_sorted([12,30,50,63,78]))'''
# Count of Frequency of Elements
'''
input :[1,2,3,2,4,3,1,5]
output:{1:2,2:2,3:2,4:1,5:1}
'''
'''
li = [1,2,3,2,4,3,1,5]
d= {}
for i in li:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)'''
li = [1,2,3,2,4,3,1,5]
d = {}
for i in li:
    d[i] = d.get(i,0)+1
print(d)