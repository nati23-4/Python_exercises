#Natalie Hannoush
#Prof. Jackson Henry
#RPS: Computational Game Theory on Network
#Side hustle: Project Euler--Problem 3

#Start date: 
#9/8/2025
#9: 52

#End date: 
#
#

#Problem 3: Largest Prime Factor
import math

x = int(input("Find the prime factors of: "))

#Jackson's solution
i = 2

def lpf(x):
    prime_factor = []
    i = 2
    while x > 1:
        if (x % i) == 0:
            x = (x/i)
            prime_factor.append(i)
            i = 2
        else:
            i+= 1
    print(prime_factor)
    print("The largest prime factor is ", max(prime_factor) ,".")
lpf(x)

    
#My function -WIP
#def prime_factor(x):
#    prime_num = [1, 2]   #function currently doesn't work for 1 and 2
#    for a in range (3, 1000):               
#        for b in range (2, math.isqrt(a)):     #range for what to divide potential prime number by; prints sqrt to the nearest int
#            if (a % b) == 0:                  #if a is divisible, it is not a prime number
#                break
#            else:                              #if a is not divisible by 2 or anything else, it is a prime number
#                prime_num.append(a)
#    prime_fact = []
#    for n in prime_num: 
#        if (x % n) == 0:
#            prime_fact.append(n)
#            return(x == (x / n))
#        else:
#            pass
#    print("The prime factors of ", x ," are ", prime_fact , ".")
#    print("The largest prime factor of ", x ," is ", prime_fact[-1] , ".")
#prime_factor(x)



#z = int(input("Integer to be factored: " ))
#p_n = [2, 3, 4, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 79, 83, 89, 97, 101]
#def p_f (z):
#    pr_f = []
#    for c in p_n:
#        if (z % c) == 0:
#            pr_f.append(c)
#            return(z == (z / c))
#        elif z != 1:
#            break 
#        else:
#            pass
#    print(pr_f)
#p_f(z)
