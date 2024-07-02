import random
from sympy import *

# Define symbols
x, u, dx = symbols('x u dx')

# Generate a random integral
f = random.choice([sin(x), cos(x), exp(x), log(x)])
a = random.randint(1, 5)
b = random.randint(-5, -1)
integral = Integral(f, (x, a, b))

# Display the initial integral
print("Initial integral:")
print(integral)

# Perform random u-substitutions
frames = []
for i in range(5):
    # Generate a random u-substitution
    u_val = random.choice([x**2, log(x), exp(x)])
    u_sub = u_val.subs(x, u)
    du = diff(u_sub, u) * dx

    # Perform the u-substitution on the integral
    new_integral = integral.subs(x, u_val) * du

    # Extract the new limits of integration
    new_a = new_integral.limit[0][1].subs(u, u_val)
    new_b = new_integral.limit[0][2].subs(u, u_val)

    # Create a new integral with the u-substitution applied
    new_integral = Integral(new_integral.args[0], (u, new_a, new_b))

    # Add the new integral to the list of frames
    frames.append(new_integral)

    # Set the new integral as the current integral for the next iteration
    integral = new_integral

# Save the frames as a GIF
animate(frames, "usub.gif", fps=1)
