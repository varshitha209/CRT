'''input:4
    output:
    * * * *
    * * * *
    * * * *
    
n=int(input())
for i in range(n):  
    for j in range(n):
        print("*",end=" ")
    print()'''
''' n=4
    *
    * *
    * * *
    * * * * write a program to print the above pattern'''
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=4
* * * *
* * *
* *
* '''
'''n=int(input())
for i in range(n):#for i in range(n,0,-1) for j in range(i)
    for j in range(n-i):#for j in range(i,n)
        print("*",end=" ")
    print()'''
''' n=4
    output:
    1
    2 3
    4 5 6
    7 8 9 10 write a program to print the above pattern'''
'''n=int(input())                  #k=1    n=int(input())
m=1                             #for i in range(1,n+1):
for i in range(n):              #   for j in rangr(i):
    for j in range(i+1):        #       print(k,end=" ")
        print(m,end=" ")        #       k+=1
        m+=1
    print()'''                   #   print()  
''' input:4
    output:
    A
    A B
    A B C
    A B C D'''
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()'''
'''print("_ _ _ _  _ _ _ _ _ __ __ _ ")
n=int(input())
k=65
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k+=1
        
    print()'''
#Hollow Square
'''n=4
* * * *
*     *
*     *
* * * *'''
