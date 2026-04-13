#Debugging --> Finding and fixing of errors
#Types of Errors : 1)Syntax Errors--> Missing of colon,Missing of identataion
                #  2)Runtime Errors->>Division by Zero
                # 3)Logical Errors -->Where Logic doesnot match exactly
# Fixing the Errors Techniques: 
# 1)print()
# 2)try-except
# 3)Using pdb
#   pdb-->Python Debugger
#   Purspose
#   1) Pause the execution code
#   2) Inspect the variable's value
#   3)To run the code by line 
#   pdb Commands
#   1)n --> To execute the output in next line
#   2)p variable--> to get the value of a variable.
#   3)I --> List nearby code 
#   4)c-->Continue the execution 
#   5)s-->to start a function 
#   6)r --> return from the function 
#   7)h-->help  
#   8)q-->Ouit the execution
#try :
 #   a = int(input("Enter a number:"))
 #   print(10/a)
#except ZeroDivisionError:
 #   print("Can not divisible by Zero.")
#except ValueError:
  #  print("Invalid Input") 
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a = int(input("Enter first number:"))
b = int(input("Enter Second number:"))
print(add(a,b))