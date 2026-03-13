#find the factors of a given number
''''def find_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
        return factors
num = int(input("Enter a number: "))
print("Factors:",find_factors(num))'''
#reverse integer in leetcode
n=int(input())
if n>=0:
    print(int(str(n)[::-1]))
else:
    n=-1*n 
    print(-1 * int(str(n)[::-1]))
    # input:6894 output:4986
    ''' another method:
    n=int(input())
    if n<0:
        n=-1*n
    print(-1*int(str(n)[::-1]))'''

