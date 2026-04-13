'''Time Complexity:
Definition: Time Complexity can be measure based upon the input
Ex:n = 10
print(n)
o(1)-->Constant Time
O(n) -->Single loop
'''
#print("Time Complexity:")
#arr = [1,2,3,4,5]
#Brute Force -->step by step execute,high complexityneglects the efficiency
# Optimal Solution -->needs thinking ,low complexity
'''def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([10,20,30,58,46],10))
print(linear_search([10,20,30,58,46],46))
print(linear_search([10,20,30,58,46],30)) '''
#Binary Search
def binary_search(arr,target):
    for i in range(len(arr)):
        low = 0
        high = len(arr-1)
        mid = (low+high)//2
        

