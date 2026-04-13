'''import numpy as np 

arr=np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even number list is:",np.arange(2,10,2))
print("Odd number list is:",np.arange(1,10,2))


n = int(input("enter the size:"))
ele = list(map(int,input("enter ele:").split()))
print("Array ele are:",np.array(ele))
nums=list(map(int,input("Enter nums:").split()))
if len(set(nums)) >=3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))'''
#Monotonic
nums=list(map(int,input("Enter nums").split()))
inc=True
dec=True 
for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        dec=False
    if nums[i]<nums[i-1]:
        inc=False 
if inc or dec:
    print("Monotonic Array")
else:
    print("not monotonic array")