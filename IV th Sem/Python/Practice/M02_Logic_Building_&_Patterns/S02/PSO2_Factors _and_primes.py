'''
Read a number from user and  Count number of factors.
'''
'''
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i,end=" ")
print(count)'''
'''
n = int(input())
if n>=0:
    print(int(str(n)[::-1]))
else:
    n = -1*n
    print(-1*int(str(n)[::-1]))'''
'''
Check if a number is prime or not.
'''
n = int(input("Enter a number: "))
if n>1:
    for i in range(2, n):
        if n % i == 0:
            print( "not a prime number")
            break
    else:
        print("Prime number")
