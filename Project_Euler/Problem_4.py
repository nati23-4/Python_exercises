Natalie Hannoush
#Prof. Jackson Henry
#RPS: Comuptational Game Theory on Network
#Side hustle: Project Euler - Problem 4

#Start Date: 
#9/14/2025
#10:00

#End Date: 
#
#

#Problem 4: Largest Palindrome Product

#A palindromic number reads the same both ways. The largest palindrome made from the product of 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindromem made from the product of 3-digit numbers. 

#Let's go :) 

def palindrome():
    for f1 in range(999,100,-1): 
        for f2 in range(999,f1-1,-1):
            print(f1,f2)
            prod = str(f1*f2)
            if prod == (prod[::-1]):
                return(prod,f1,f2)
print(palindrome())

#Try #1. Let's try it out. 
        
        

