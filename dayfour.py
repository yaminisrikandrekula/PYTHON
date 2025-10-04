list=[1,2,3,4,5,6,7,8,9]
print(list[4:8])

list=[1,2,3,4,5,6,7,8,9]
print(list[4:])

list=[1,2,3,4,5,6,7,8,9]
print(list[1::2])

list=[1,2,3,4,5,6,7,8,9]
print(list[0::3])

def mom (a,b):
    print(a+b)
a=10
b=20
c=mom(a,b)
print(c)

if True:
    print("Valid")
else:
    print("Invalid")
    
if False:
    print("Valid")
else:
    print("Invalid")
    
try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result =a+b
    print("sum:", result)
except valueError:
    print("Invalid input!please enter number only.")

try:
    num=int(input("Enter a number:"))
    result = 10/num
    print("Result:", result)
except valueError:
    print("Invalid input!please enter number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An error occupied:",e)
finally:
    print("Execution finished.")
