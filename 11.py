# Author : Rahul Sinha (boywho.codes)
# Date : 26-12-2021 18:00 IST
# Website : https://rahulsinha.co
# Contact : rahulsinhaoff@gmail.com , https://instagram.com/boywho.codes
# Interpreter : Python 3.9.6 64-bit

lst = []

n = int(input("Enter number of elements : "))
 

for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) 
     


print(sum(lst)/n)