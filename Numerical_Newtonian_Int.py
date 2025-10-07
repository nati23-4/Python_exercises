#Natalie Hannoush
#Prof. Jackson Henry
#ISU: RPS Game Theory Netweork Research
#Problem 3: Numerical Newtonian Integrator (Longer exercise)

#Start date: 
#9/5/2025
#14:22

#End date: 
#
#

#Problem:
#In classical mechanics, Newton’s second law states:

#F = m a where a = \frac{d^2x}{dt^2}

#Task:

#Write a Python program that simulates the motion of a particle in 1d under a constant force (like gravity).

#Start with initial conditions: mass m, position x0, velocity v0, and a constant force F.

#Use a small time step dt and update the velocity and position step by step.

#Run the simulation for some duration T and output the trajectory of the particle.

#Plot the trajectory using matplotlib.

#Bonus!

#Modify your code to work in 2d using numpy arrays as vectors.

#m = float(input("Initial mass (kg): "))
#x_0 = float(input("Initial position (m): "))
#v_0 = float(input("Initial velocity (m/s): "))
#constant_force = float(input("Constant force (gravity = 9.8 m/s^2 unless otherwise specified"))
#runtime = float(input("Run time (s): "))
#dt = float(input("Time step dt: "))

#def Newtonian_Int (m, x, v, F):
    #dt = 0.5
    #not sure where to go from here, will sketch it out 

    #and we're back, nearly a month later :) Jackson sent me on a side quest to Project Euler until I was ready. The day has come. I will finally write this program

    #Full disclosure, my intermech professor lowkey did this in class the other day, but I'm not referencing the code and trying to work it out myslef. 
#If we have less inputs & set system at rest at t=0

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplot.use('TkAgg')

mass = 50 #kg
x_0 = 10 #m
v_0 = 0 #m/s
constant_force = 9.8 #m/s^2
runtime = 10 #s
dt = 0.1 #timestep

#I guess these have to be defined as well
x = 0
v = 0
t = 0 #so that I don't get errors for the functions below lol

#... I guess technically the mass doesn't matter?

#attempt: isolating the velocity & position functions to test if they work individually 
#Velocity calculator
def velocity_calculator(v,a):
    dv = a*dt
    v = v + dv
    return(v)

#Position
def position_calculator(x,v):  
    dx = v*dt
    x = x + dx
    return(x)
    
velocity = [0]
position = [0]
runtime = 10 #s

#Integration
def Newtonian_Integrator():
    mass = 50 #kg
    x_0 = 10 #m
    v_0 = 0 #m/s
    constant_force = 9.8 #m/s^2
   # runtime = 10 #s
    dt = 0.1 #timestep
    x = 0
    v = 0
    t = 0
    a = 9.8 
    for t in  np.arange(0,runtime,dt):
       # print(t)
        v = velocity_calculator(v,a)
        x = position_calculator(x,v)
        velocity.append(v)        
        position.append(x)
       # print(velocity)
       # print(position)
Newtonian_Integrator()

time = list(np.arange(0,runtime+dt,dt))

#Plotting :)

#velocity
plt.plot(time,velocity) #x,y
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Graph of velocity over time.')
plt.ion()
#print(len(time),len(velocity))
plt.show()

plt.savefig('Velocity_plot.png')

#position
