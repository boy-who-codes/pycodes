# Author : Rahul Sinha (boywho.codes)
# Date : 26-12-2021 18:00 IST
# Website : https://rahulsinha.co
# Contact : rahulsinhaoff@gmail.com , https://instagram.com/boywho.codes
# Interpreter : Python 3.9.6 64-bit

num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    
