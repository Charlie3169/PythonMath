import math
import cmath
from fractions import Fraction
import sympy as sym


# Returns a phasor with a phase of 2pi / denominator
# Ex: genericAlternator(3) = e^2πi / 3
def genericAlternator(denominator):
    return cmath.exp((math.tau * complex(0, 1)) / denominator)

def genericAlternatorSymbolic(denominator):
    return sym.exp((sym.tau * sym.I) / denominator)


def genericAlternatorPower(numerator, denominator):
    return cmath.exp((math.tau * complex(0, 1) * numerator) / denominator)


def genericAlternatorSeries(period, n):
    sum = complex(0,0)

    for x in range(1, n + 1):        

        sum += 1 / x        

    return sum



output = genericAlternator(3)
#print("Value: ", output)
#print("Polar: ", cmath.polar(output))
#print("Modulus: ", abs(output))
#arc = (math.atan2(output.imag, output.real) / (2 * math.pi))
#print("Argument: ", Fraction(arc) , "τ")


for i in range(0, 7):
    a = genericAlternatorPower(i,6)
    print(math.atan2(a.imag, a.real))

print("Space")

for j in range(0,3):
    print(genericAlternatorPower(j,3) * genericAlternatorPower(j,3) * genericAlternatorPower(j,3))
