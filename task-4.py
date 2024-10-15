"""Author:Savio Bijo Thomas
   date-15-10-2024
   purpose:To determine the smallest among three numbers"""

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num3 and num1>num2 :
    print(num1,"is greater.")
elif num2>num3 and num2>num1 :
    print(num2,"is greater.")
else:
    print(num3,"is greater")
