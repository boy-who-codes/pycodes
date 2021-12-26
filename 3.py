# Author : Rahul Sinha (boywho.codes)
# Date : 26-12-2021 18:00 IST
# Website : https://rahulsinha.co
# Contact : rahulsinhaoff@gmail.com , https://instagram.com/boywho.codes
# Interpreter : Python 3.9.6 64-bit

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   biggest = num1
elif (num2 > num1) and (num2 > num3):
   biggest = num2
else:
   biggest = num3
 
print("The biggest number is",biggest)
