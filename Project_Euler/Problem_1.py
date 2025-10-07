#Natalie Hannoush
#Prof. Jackson Henry
#RPS: Computational Game Theory on Network
#Side quest: Python via project Euler --Problem 1

#Start date: 
#9/5/2025
#14:40

#End date:
#9/5/2025
#15:26

#Total time:
#46 mins

#Problem 1
#Multiples of 3 or 5

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23

#Find: sum of all multiples of 3 or 5 below 1000

#Note (my note): Very similar to FizzBuzz

#one_thousand = range[0, 10001]
#sum_val = 0

def sum_of_multiples():
    multiples = []
    for n in range(1, 1000):
        if (n % 3) == 0:
            multiples.append(n)
        elif (n % 5) == 0:
            multiples.append(n)
        else:
            pass
    total = sum(multiples)
    print(total)
sum_of_multiples()

#Initially, I tried to solve this problem by creating a variable var_sum that would get updated with each multiple. But that wasn't really working, and I quickly realized that I'd rather make a list of multiples and take the sum at the end. Not sure which way is better, but I'm happy with my progress :)

        
