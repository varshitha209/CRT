'''
Docstring for IV SEM.Python.Practice.M02_Logic_&_Programming_Basis.S01.PS01_Digit_Problems
1) Write  python code to count the digits of number ?
Ex:15678 --> output:5
2) sum of the digits of a number?
Ex: 12345--> 1+2+3+4+5=15
3)Product of the digits of a number?
4)Reverse the number
5)Count the even and odd digits
#1
num= 15678
count = len(str(num))
print(f"Number of digits: {count}")
#2
num=12345
d_s=sum(int(digit) for digit in str(num))
print(f"Sum of digits:{d_s}")
#3
num=int(input())
sum=1
while num>0:
    sum *=num%10
    num//=10
print(sum)'''
#4
num=int(input("Enter a number:"))
rev=0
while num>0:
    digit =num%10
    rev=rev*10+digit
    num//=10
print("Reversed number:",rev)
    
