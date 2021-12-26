# Author : Rahul Sinha (boywho.codes)
# Date : 26-12-2021 18:00 IST
# Website : https://rahulsinha.co
# Contact : rahulsinhaoff@gmail.com , https://instagram.com/boywho.codes
# Interpreter : Python 3.9.6 64-bit

nterms = int(input("No of Terms "))
num1, num2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(num1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(num1)
       nth = num1 + num2

       num1 = num2
       num2 = nth
       count += 1
       
