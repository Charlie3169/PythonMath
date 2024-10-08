import cmath
import math
import time
from RootsOfUnity import rootOfUnityPower

# The modulo operator is a super important concept in math and computer science
# This program approximates the modulo operator using mathmatical properties of complex numbers
# Pretty useless but its a cool application of math

# a mod b = t mod c
# t: Value (imagine a line) to be wrapped around circle
# c: Effective circumference of the circle
# Doesn't work for very large numbers due to the precision falling off for pi and e
def complexMod(t, c):

    # e^(2pi * i) wraps around the circle once, so by scaling the 2pi by the the circumerence we can get a 1/c turn, 
    # which can then be scaled by t to any whole number ratio of the circumference
    result = rootOfUnityPower(t, c)
    
    # This gets the angle of the result and converts it from atan2's range (-pi, pi) to (0, 2pi)
    angle = math.atan2(result.imag, result.real)
    if(angle < 0): angle += cmath.tau 

    # Take the angle and divide it by 2pi radians times the circumference to get 
    # The numerator ratio of how far it has travelled around the circle   
    return (c / cmath.tau) * angle


# a mod b = x mod modulo
# Approximates a mod b using a modified complex fourier series of a sawtooth wave
# Matches the mod function when a mod b != 0, and is b/2 when a mod b == 0
def fourierSeriesModFunction(x, modulo, precision):
    sum = complex(0,0)
    for n in range(1, precision):
        currentTerm = rootOfUnityPower(x*n, modulo) / n        
        sum += currentTerm

    return (modulo / 2) - (modulo / math.pi) * sum.imag

a = 11312412
b = 5500

print('\n')
start = time.time()
print("Modular result using complex unit circle: ", complexMod(a, b))
end = time.time()
print(f'Runtime: {end - start} seconds \n')

start = time.time()
print("Modular result using fourier series: ", fourierSeriesModFunction(a, b, 100000))
end = time.time()
print(f'Runtime: {end - start} seconds \n')

start = time.time()
print("Modular result using normal mod operator: ", a % b)
end = time.time()
print(f'Runtime: {end - start} seconds \n')