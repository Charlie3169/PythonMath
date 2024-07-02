from sympy import symbols, expand

z, C = symbols('z C')
P = lambda n: (z + C)**n

def mandelbrot_expansion(n):
    if n == 1:
        return P(2)
    
    previous_expansion = mandelbrot_expansion(n - 1)
    return expand((previous_expansion + C)**2)

iterations = 3

for i in range(1, iterations + 1):
    expansion = mandelbrot_expansion(i)
    print(f"µ_{i} = {expansion}")
