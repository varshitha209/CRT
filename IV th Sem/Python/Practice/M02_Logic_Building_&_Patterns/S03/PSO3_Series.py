'''
Read  a and b and print the series of arithmetic progression

a = int(input())
b = int(input())
for i in range(10):
    d = a + (i*b)
    print(d,end=" ")
'''
a = int(input())
l = len(str(a))
res = 0
for i in str(a):
    res += int(i)**l 
print("Armstrong Number" if res == a else "Not an Armstrong Number")