#Natalie Hannoush
#Prof. Jackson Henry
#ISU: RPS Computational Game Theory on Network
#Side project: Project Euler - Problem 5 

#Start Date: 
#9/30/2025
#12:50

#End Date: 
#9/30/2025
#13:41

#Problem 5: Sum Square Difference

#The sum of teh squares of the firs ten natural numbers is

# 1^2 + 2^2 + ... + 10^2 = 385

#The square of the sum of the first ten natural numbers is, 

# (1 + 2 + ... + 10)^2 = 55^2 = 3025

#Hence the difference between the sum of thes quares of teh first ten natural numbers and the square of the sum is 3025 - 385 = 2640. 

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. 

#Let's go :) 

#1. Sum of squares


def sum_of_squares(highest_val):
    squares = []
    for n in range(1,highest_val):
        squares.append(n**2)          #notation for squaring in py
    return(sum(squares))

#2. Sum of sum^2
def square_of_sum(highest_val):
    one_hundred = list(range(1,highest_val))
    # print(one_hundred)
    return(sum(one_hundred)**2)
# print(sum(one_hundred)**2)

def difference(highest_val):                #always range(1, max)
    print(square_of_sum(highest_val) - sum_of_squares(highest_val))
difference(101)

#Function --> Take in, transport, & give back out
#most of the time should have a return val
#mutates data


