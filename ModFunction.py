import cmath
import math

# Program to calculate the modulus operator using mathmatical properties of complex numbers
# Pretty useless but its a cool application of math
# a mod b = t mod c
# t: Value to be wrapped around circle
# c: Circumference of a circle
# Doesn't work for very large numbers due to the precision falling off
def complexMod(t, c):

    # e^(2pi * i) wraps around the circle once, so by scaling the 2pi by the the circumerence we can get a 1/c turn, 
    # which can then be scaled by t to any whole number ratio of the circumference
    result = cmath.exp((cmath.tau / c) * complex(0,1) * t)

    # Get the angle of the complex result and divide it by 2pi radians times the circumference to get 
    # the numerator ratio of how far it has travelled around the circle    
    return round((c / cmath.tau) * (math.atan2(result.imag, result.real)))

t = 10
c = 6

print("Modular result using complex circle: ", complexMod(t, c))
print("Modular result using mod operator: ", t % c)

