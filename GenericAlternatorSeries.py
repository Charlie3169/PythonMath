import math
import cmath
from fractions import Fraction
import sympy as sym


# Returns a phasor with a phase of 2pi / denominator
# Ex: genericAlternator(3) = e^2πi / 3
def rootOfUnity(denominator):
    return cmath.exp((math.tau * complex(0, 1)) / denominator)

def rootOfUnitySymbolic(denominator):
    return sym.exp((sym.tau * sym.I) / denominator)


def rootOfUnityPower(numerator, denominator):
    return cmath.exp((math.tau * complex(0, 1) * numerator) / denominator)


def genericAlternatorSeries(period, n):
    sum = complex(0,0)    

    for x in range(1, n + 1):        

        sum += 1 / x        

    return sum

def extendedModFunction(x, modulo, precision):
    print(x)

def randomPolynomial(x):
    print(x)

def taylorSeries(function, x, a, depth):
    #Needs a lot of work
    sum = sym.Poly(0)
    for k in range(1,depth):
       sum += function.diff(x,k)*(x - a)**k / (math.factorial(k))
    print(sum)

def newtonsMethod(function, epsilon):
    last = 0
    diff = 0
    while(diff > epsilon):
        #Do newtons 
        print("poop")
    print(last)


output = rootOfUnity(3)
#print("Value: ", output)
#print("Polar: ", cmath.polar(output))
#print("Modulus: ", abs(output))
#arc = (math.atan2(output.imag, output.real) / (2 * math.pi))
#print("Argument: ", Fraction(arc) , "τ")


for i in range(0, 7):
    a = rootOfUnityPower(i,6)
    print(math.atan2(a.imag, a.real))

print("Space")

for j in range(0,3):
    print(rootOfUnityPower(j,3) * rootOfUnityPower(j,3) * rootOfUnityPower(j,3))
