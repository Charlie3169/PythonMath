import sympy as sp

# Define the large integer n1
n1 = 123456789012345678901234567890

# Estimate the base b1 such that b1^2 is roughly the same order as n1
# We use the square root of n1 to determine the base estimate
base_estimate = int(n1 ** 0.5)

# Compute d1 and remainder r1 using base_estimate
d1 = n1 // base_estimate
r1 = n1 % base_estimate

# Define the symbolic variable for polynomial fitting
x = sp.symbols('x')

# Generate sample points for fitting the polynomials
# Slightly vary r1 to get different samples
sample_points = [
    (r1 - 1, (n1 // (base_estimate - 1)), (base_estimate - 1)),
    (r1, d1, base_estimate),
    (r1 + 1, (n1 // (base_estimate + 1)), (base_estimate + 1))
]

# Extract (r, d) points for fitting p1(x)
div_points = [(r, d) for (r, d, b) in sample_points]

# Extract (r, b) points for fitting p2(x)
base_points = [(r, b) for (r, d, b) in sample_points]

# Fit polynomials p1(x) and p2(x) using the sample points
div_poly = sp.interpolate(div_points, x)
base_poly = sp.interpolate(base_points, x)

# Multiply div_poly and base_poly to get prod_poly
prod_poly = sp.expand(div_poly * base_poly)

# Add the +x term to prod_poly to get the final p3
final_poly = sp.expand(prod_poly + x)

# Output the polynomials and the remainder
print(f"p1(x) = {div_poly}")
print(f"p2(x) = {base_poly}")
print(f"p3(x) = {final_poly}")
print(f"r1 = {r1}")

# Verification: reconstruct n1
n1_reconstructed = final_poly.evalf(subs={x: r1})
print(f"Reconstructed n1: {n1_reconstructed}")
