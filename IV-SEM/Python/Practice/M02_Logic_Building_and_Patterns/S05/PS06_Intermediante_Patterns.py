'''li=[1,2,3,4,5,6]
   output=[ 1,4,9,16,25] 
li=[1,2,3,4,5,6]
output=[i**2 for i in li if i%2!=0]
#print only even numbers from my list
li=[1,2,3,4,5,6]
output=[i for i in li if i%2==0]
print(output)

li = ['a','b','c']
#'a b c'
res =  ""
for ch in li:
    res+=ch+" "
print(res) 
or
print(" ".join(li))
'''
'''3.Diamond Pattern
n=4  output:
    *
   * *
  * * *
 * * * * 
  * * *
   * *
    * '''

'''
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)'''
#write the code 
'''output:
    1 
   1 2
  1 2 3
 1 2 3 4'''
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()'''
#write above code using list comprehension
'''n=int(input())          
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()'''
#n=int(input())
'''for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(k) for k in range(1,i+1)]))'''
'''output:
    1 
   2 2
  3 3 3
 4 4 4 4'''
'''n=int(input())
for i in range(1,n+1):      
    print(" "*(n-i)+" ".join([str(i) for k in range(1,i+1)]))'''
'''Butterfly Pattern
n=4 
output:
*      *
**    **  
***  ***
********
********
***  ***
**    **
*      *'''
n=int(input())
for i in range(1,n+1):      
    print("*"*i+" "*(2*(n-i))+"*"*i)
 