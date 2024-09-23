a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print("Available operations in this simple calculator: '+','-','*','/' ")
operation=input("Enter the operation to be performed: ")

if operation == '+':
  print("Result:",a+b)
  
elif operation == '-':
  print("Result:",a-b)
  
elif operation == '*':
  print("Result:",a*b)
  
elif operation == '/':
 if b != 0:
   print("Result:",a/b)
 else:
   print("Undefined")
   
else:
  print("INVALID OPERATION")
