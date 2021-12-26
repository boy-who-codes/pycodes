# Author : Rahul Sinha (boywho.codes)
# Date : 26-12-2021 18:00 IST
# Website : https://rahulsinha.co
# Contact : rahulsinhaoff@gmail.com , https://instagram.com/boywho.codes
# Interpreter : Python 3.9.6 64-bit
# Problem Statement : Create a menu driver program to apply all the method/function of the list

lst = []
while True:
    print("-------------------------------------------")
    print("Choose you option from the following")
    print("0. Show the elements of list")
    print("1. Appends object to list ")
    print("2. Sort the list")
    print("3. Clear the  list")
    print("4. Reverses objects of list ")
    print("5. Returns the index of the element in the list")
    print("6. Update the list")
    print("7. Returns count of how many times element occurs in list [count()]")
    print("8. Number of Elements in the list ")
    print("9. Extends the list with another list [extend()]")
    print("10. Insert element at specific index")
    print("11. Exit")
    inp = int(input("\nenter your option number : "))
 
    
    if inp == 0:
        print(lst)
        
    elif inp == 1:
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = (input())
            lst.append(ele) 
            
    elif inp == 2:
        if len(lst) == 0:
            print("first enter some elements in the list ")
        else:
            lst.sort()
    elif inp == 3:
        lst.clear()
    
    elif inp ==4:
        if len(lst) == 0:
            print("first enter some elements in the list ")
        else:
            lst.reverse()
    elif inp ==5:
        print("enter the element whose index is to be printed")
        print(lst)
        ans = (input(">"))
        print(lst.index(ans))
    
    elif inp ==6:
            ele = (input("enter your new element "))
            lst.append(ele) 
         
    elif inp == 7:
        print("enter the element ")
        print(lst)
        ans = (input(">"))
        print(ans,"occurs" ,lst.count(ans) , "times in list")
    
    elif inp == 8:
        print(len(lst))   
    
    elif inp == 9:
        n = int(input("Enter number of elements to create new list: "))
        for i in range(0, n):
            ele = (input())
            lst.extend(ele) 
     
    elif inp == 10:
        print(lst)
        elem = input("enter the element \n >") 
        index = int(input("enter the index \n >"))     
        lst.insert(index , elem)
        print(lst)
        
        
    elif inp == 11:
        print("Exiting the program")
        break
    
    else:
        print("Wrong option ! try again")
    
    
       