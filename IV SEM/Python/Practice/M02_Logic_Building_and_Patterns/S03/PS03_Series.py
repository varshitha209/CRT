'''a=1 d=2
1,3,5,7,9,11,...
a,a+d,a+2d,a+3d,..
a+0*d
a+1*d
a+2d  for
a+9d
#display Arithematic progression values upto 10
a=int(input())
d=int(input())
for i in range(10):
    print(a+(i*d),end=" ")
    Fibbonacci Series ==>0,1
        n values 
        n=5
        0 1 1 2 3 
#2)Fibonnaci series
a=0
b=1
n=int(input())
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b 
n=int(input())
li=[0,1]
for i in range(2,n):
    li.append(li[i-2+li[i-1]])
print(li)'''
#Power of a number
n=int(input())
for i in range(1,11):
    print(n**i,end=" ")


