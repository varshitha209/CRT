'''n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
    i=1
    while i<=n:
        print(i,end=" ")
        i+=1
name="Srivally"
for ch in name:
    print(ch,end=" ")
    i=0
    while i<1:
        print(name,end=" ")
        i +=1
name="Srivally"
for i in range(len(name)):
    print(i,name[i])
name="Srivally"
for i in range(len(name)-1,-1,-1):
    print(name[i],end=" ")'''
n=int(input())
for i in range(1,n+1):
    if i==5:
        break
    print(i,end=" ")

'''loop control statements:
break-->stop
continue-->skip
pass-->nothing'''