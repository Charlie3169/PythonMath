import math
import cmath
import sympy as sym
from sympy import init_printing
init_printing()

# Returns a phasor with a phase of 2pi / denominator
# Ex: genericAlternator(3) = e^2πi / 3
def rootOfUnity(denominator: int) -> complex:
    return cmath.exp((math.tau * complex(0, 1)) / denominator)



def rootOfUnitySymbolic(denominator: int) -> sym.Symbol:
    return sym.exp((2 * sym.pi * sym.I) / denominator)


def rootOfUnityPower(numerator: int, denominator: int) -> complex:
    return cmath.exp((math.tau * complex(0, 1) * numerator) / denominator)

def rootOfUnityPowerSymbolic(numerator: int, denominator: int) -> sym.Symbol:
    return sym.exp((2 * sym.pi * sym.I * numerator) / denominator)


def rootOfUnityZetaSeries(nthRoot, s : complex, precision: int) -> complex:
    sum = complex(0,0)    
    for n in range(1, precision + 1):     
        sum +=  rootOfUnityPower(n, nthRoot) / (cmath.exp(s * cmath.log(n)))        
    return sum

# def nthCyclicalAlternatorZetaSeries(precision: int):
    sum = complex(0,0)    
    for x in range(1, precision + 1):     
        sum += 1 / (cmath.exp(s * cmath.log(x)))       

    return sum

    







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



#for i in range(0, 7):
#    a = rootOfUnityPower(i,6)
#    print(math.atan2(a.imag, a.real))

#print("Space")

#for j in range(0,3):
#    print(rootOfUnityPower(j,3) * rootOfUnityPower(j,3) * rootOfUnityPower(j,3))


#print(latex(rootOfUnityPowerSymbolic(5, 7)))
print(rootOfUnityZetaSeries(1,2,10000))
print(math.pi * math.pi / 6)
print(rootOfUnityZetaSeries(2,1,10000))
print(math.log(2))
