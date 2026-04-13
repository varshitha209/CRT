'''Time Complexity:
Defination: Time Complexitycan be measure based upon the input 
ex: n=10
print(n)
o(1) --> constant time complexity
o(n) --> simgle loop'''
'''Brute Force --> step by step execute,high complexity,neglecting the efficiency
Optimal Solution --> needs thinking,low complexity'''
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([10,20,30,58,46],10))
print(linear_search([10,20,30,58,46],46))
print(linear_search([10,20,30,58,46],30))