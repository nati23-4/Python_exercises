#Natalie Hannoush
#Prof. Jackson Henry
#ISU: RPS - Computational Game Theory on Network
#Side Hustle: Project Euler - Project #5

#Start Date (since opening):
#9/24
#11:34

#End Date:
#
#

#Project 5: Smallest Multiple
#2520 is the smallest number that can be divided by eacah of the numbers from 1 to 10 without any remainder. 

#What is the samllest possible number that is evenly divisble by all of the numbers from 1 to 20? 

def smallest_number():
    number = 1
    #for number in range(1, n +2):
    while True:
        for divisor in range(2, 21):
           # print('number: ', number)
            if (number % divisor) != 0:     #not equal to 0
                break
            else:
                if divisor == 20:
                    return(print("The smallest number divisible by the numbers ", 1 ," through ", 20 ," is ", number ,"."))
           # if (number % divisor) == 0:
           #     print(number % divisor)
           #     if divisor == 10:
           #         return("The smallest number divisible by the numbers ", 1 ," through ", 20 ," is ", number ,".")
           # else: 
           #     break
        number += 1
       # print(number)
smallest_number()
       
#It works!
