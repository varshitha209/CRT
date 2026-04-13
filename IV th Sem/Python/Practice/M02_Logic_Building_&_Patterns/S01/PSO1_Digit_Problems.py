'''
1. Write a Python code to count the digits of number?
Ex:15678 -->Output :
'''
n = int(input("Enter a number:"))
count = 0
while n>0:
    n = n//10
    count = count + 1   
print("The number of digits in the given number is:",count)
'''
2.Write a python code to find the sum of digits of a number?
Ex: 1234 -->Output : 10
'''
n = int(input("Enter a number:"))
sum = 0 
while n>0:
    digit = n%10
    sum = sum + digit 
    n = n//10
print("The sum of the digits in the given number is:",sum)
'''
3.Write a python code to find the product of digits of a number?
Ex: 1234 -->Output : 24'''
n = int(input("Enter a number:"))
product = 1
while n>0:
    digit = n%10
    product = product * digit 
    n = n//10
print("The product of the digits in the given number is:",product)
'''
4.Write a python code to find the reverse of a number?
Ex: 1234 -->Output : 4321'''
n = int(input("Enter a number:"))
reverse = 0
while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n = n//10
print("The reverse of the given number is:",reverse)
'''
5.Write a python code to count the even and odd digits?
Ex: 1234 -->Output : Even digits: 2, Odd digits: 2
'''
n = int(input("Enter a number:"))
even  = 0
odd = 0
while n>0:
    n =n//10
    digit = n%10
    if digit%2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even digits:",even)
print("Odd digits:",odd)
'''
6.Write a python code to print the largest digit of a number
Ex: 3291 -->Output : 9
'''
n= int(input("Enter a number:"))
large = 0
while n>0:
    digit = n%10
    if digit > large:
        large = digit
        n = n//10
print("The largest digit in the given number is:",large)