#Natalie Hannoush
#WPI
#Dr. Jackson Henry
#ISU: RPS Computational Game Theory on Network 
#Test 1: Can I do python? (FizzBuzz) 

#Date Start:
#8/27/2025
#9:23

#Date End: 
#8/27/2025
#11:11 

#FizzBuzz
#Problem:
#Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

#Tip, consider the remainder/"mod" operator %

for n in range(1, 101):                    #n = number, range = list of n's
    if ((n % 3) == 0) and ((n % 5) == 0):  #conditional for mults of 3 & 5
        print ("FizzBuzz")                  
    elif (n % 3) == 0:                     #cond. for mults of 3
        print ("Fizz")
    elif (n % 5) == 0:                     #cond. for mults of 5
        print ("Buzz")
    else:                                  #if N/A, just print "n"  
        print (n)

#Solution: using a loop (for), to create a list (range(start, end)) with a conditional if/else statement.                                                                                                                           #In other words, using a loop to cycle the same conditionals through each number in a list of 100 (from 0 to 100)

#Notes/issues: 
#Apparently (n & 3) is taking out multiples of four, not multiples of three. Maybe this leads from an incomplete understanding of the mod operator (%). Hmm. 
#Okay, never mind. Turns out I was using "&" instead of "%." Once I switched it, everything worked :) Yayyy brainpower. 

#Initial work that was not used, but is useful to see for thought process:
#numbers_100 = list (range(1, 100))
#Fizz = (100 & 3)
#print (numbers_100)

#trying to see if I can use an if/else statement
#if (n & 3) = 0 AND (n & 5) = 0:
   # print ("Fizz")
#elif (n & 5) = 0:
  #  print ("Buzz") 
#else: 
 #   print (n)

#print("Attempt 1: Can I combine a loop and an if/else statement?")
#print("Well, if you got this far, then yes, yes you can :) ")

print("Congrats! You did it :)")
