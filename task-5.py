"""Author:Savio Bijo Thomas
   date-15-10-2024
   purpose:to determine the entry fee in a zoo"""

age=int(input("enter you age:"))
if age<10 :
    print("ticket fair is $7")
elif age>=10 and age<60:
    print("ticket fair is $10")
elif age>=60 :
    print("ticket fair is $5")
else:
    print("enter your correct age")