# Author : Rahul Sinha (boywho.codes)
# Date : 26-12-2021 18:00 IST
# Website : https://rahulsinha.co
# Contact : rahulsinhaoff@gmail.com , https://instagram.com/boywho.codes
# Interpreter : Python 3.9.6 64-bit

import calendar

inp = int((input("enter month's number")))

print("The original month number is : " + str(inp))

output = calendar.month_name[inp]

print("Month Name: " + str(output))
input()