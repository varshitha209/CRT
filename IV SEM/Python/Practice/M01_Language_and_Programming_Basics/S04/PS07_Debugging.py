''' debugging in python:
bugss --> Errors
Debugging --> Finding and fixing errors
Types of errors:
1)Syntax errors-->Missing of colon ,missing of identation
2)Runtime errors-->Division by zero 
3)Logical errors-->Missing of logics
Debugging Techniques :
        1)print()
        2)try-except
        3)Using pdb
        pdb --> python debugger
            1)pause the execeution code
            2)inspect the variables's value
            3)To run the code line by line 
            pbb commands:
                1)n --> To execute the output in a next line
                2)p variable-->to get the value of a variable
                3)L-->list near by
                4)c-->continue the execution
                5)s-->to start a function
                6)r-->return from the function
                7)h->help
                8)q-->Quit the execution
                '
try:
    a=int(input())
    print(10/a)
except ZeroDivisionError:
    print("Cannot divisible by zero")
except ValueError:
    print("Invalid input")'''
import pdb
def add(a,b):
    pdb.set_trace()#set the breakpoint
    return a+b
a=int(input("enter a 1st num:"))
b=int(input("enter a 2nd num:"))
