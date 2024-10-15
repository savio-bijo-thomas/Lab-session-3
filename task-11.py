"""Author:Savio Bijo Thomas
   date-15-10-2024
purpose:find the sum of digits of a number"""
num=int(input("enter the number"))
sum=0
while num>0 :
    remainder=num%10
    sum=sum+remainder
    num=num//10
print(sum)