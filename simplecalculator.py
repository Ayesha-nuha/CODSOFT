num1=int(input("Enter the value of Num 1: "))
num2=int(input("Enter the value of Num 2: "))
print("Available operations in this simple calculator: '+','-','*','/' ")
operation=input("Enter the operation to be performed: ")

if operation == '+':
  print("Result:",num1+num2)
  
elif operation == '-':
  print("Result:",num1-num2)
  
elif operation == '*':
  print("Result:",num1*num2)
  
elif operation == '/':
 if num2 != 0:
   print("Result:",num1/num2)
 else:
   print("Undefined")
   
else:
  print("INVALID OPERATION")
