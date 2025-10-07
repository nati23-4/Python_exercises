#Natalie Hannoush
#Dr. Jackson Henry
#ISU: RPS Computational Game Theory on Network
#Exercise 2: Collatz Conjecture

#Start Date:
#8/27/2025
#16:47

#End Date:  
#9/5/2025
#14:11

#Collatz Conjecture
#Problem:
#The Collatz sequence is defined as follows:
#Start with any positive integern\.
#If n is even, divide it by 2.
#If n is odd, multiply it by 3 and add 1.
#The colatz conjecture states that every sequence of this type will eventually reach 1. This has not been proven, but it has been true for every sequence tested.
#For example, starting with n = 6 gives the sequence:
#6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

#Task:
#Write a function that takes an integer n as input and returns the full Collatz sequence as a list.
#Make sure to test that the code is behaving as expected. Test edge cases such as the user giving 0 or giving the wrong data type.
#(Optional extra) Find the number between 1 and 1000 that produces the longest Collatz sequence.

n = int(input("Starting integer: "))
#a = int(input("Better starting integer "))

#def AGH (a): 
#    def even (a): 
#        a / 2
#    def odd (a):
#        (a * 3) + 1
#        print(a)
#    while a == int:
#        if a == 1:
#            break
#        elif a < 1:
#            print("Error. Please enter a positive integer.")
#        elif (a % 2) == 0:
#            print(even)
#        else:
#            print(odd)
#print(AGH(a))
#result = AGH(a)
#print(result)

#odd = (n * 3) + 1
#even = (n / 2)

#9/2: Trying out a function; defining odd and even inside
#9/5 better to define them globally (outside)
def even(n): 
    return(n / 2)

def odd(n):
    return((n * 3) + 1)

def Cltz_Cnj(n):
    cltz_sq = [n]
    while n != 1: 
        if n < 1: 
            print("Error. Please enter a positive integer.")
            cltz_sq.clear()
            break
        elif (n % 2) == 0:
            n = (even(n))
            cltz_sq.append(n)
        else:
            n = (odd(n))
            cltz_sq.append(n)
    print(cltz_sq)
Cltz_Cnj(n)

#def C_P():
 #   print("Congrats! You're all done with Collatz Conjecture for ", n, " :)")

#result = Cltz_Cnj(n)
#print(result)
#print(Cltz_Cnj(n)) 

#C_P

#while n == float:
 #   if n == 1: 
 #       print("The end :)")
 #       break
 #   elif n < 1 and n ==float:
 #       print("Error. Please enter a positive integer.")
 #   elif (n % 2) == 0:
 #       print(even)
 #   else:
 #       print(odd)

#while n > (-1):
#    if n == 0:
#        print ("Error: Cannot compute")
#    elif (n % 2) == 0:
#        print (even)
#    elif n == 1:
#        print("The end :)")
#        break 
#    else:
#        print (odd)
   # i += 1
  
   # elif i == 1:
   #     break
   # i += 1

#def my_func(arg):
#    while 
#for n in n :
 #   if (n % 2) == 0:
 #       print (even)
 #   else: 
 #       print (odd)
    
