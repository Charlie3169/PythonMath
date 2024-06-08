import math
import numpy as np
import matplotlib.pyplot as plt

def is_power(m):
    """ Check if a number m can be expressed as x^b for integers x and b. """
    max_b = int(math.log2(m)) + 1
    for b in range(1, max_b + 1):
        x = round(m ** (1 / b))
        if x ** b == m:
            return True, x, b
    return False, None, None

def succinctness_score(n, delta):
    """ Calculate the succinctness score of n by considering nearby numbers. """
    candidates = []
    for m in range(n - delta, n + delta + 1):
        if m <= 0:
            continue
        is_pow, x, b = is_power(m)
        if is_pow:
            # Calculate information savings
            bits_m = math.ceil(math.log2(m))
            bits_x = math.ceil(math.log2(x))
            bits_b = math.ceil(math.log2(b))
            info_savings = bits_m - (bits_x + bits_b)
            candidates.append((info_savings, abs(m - n)))
    
    if not candidates:
        return math.ceil(math.log2(n))
    
    # Calculate weighted average of information savings
    total_weight = sum(1 / (d + 1) for _, d in candidates)
    weighted_savings = sum(info_savings / (d + 1) for info_savings, d in candidates)
    
    average_savings = weighted_savings / total_weight
    bits_n = math.ceil(math.log2(n))
    expected_bits = bits_n - average_savings
    
    return expected_bits

# Calculate and plot the succinctness score for a range of n
delta = 10
n_values = range(1, 100001)
scores = [succinctness_score(n, delta) for n in n_values]

# Calculate baseline bits needed (log2(n)) and natural log of n
log2_values = [math.log2(n) for n in n_values]
ln_values = [math.log(n) for n in n_values]

# Create and save the plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, scores, label='Expected Minimum Information (bits)')
plt.plot(n_values, log2_values, label='log2(n)', linestyle='--')
plt.plot(n_values, ln_values, label='ln(n)', linestyle='--')
plt.xlabel('n')
plt.ylabel('Bits / Information')
plt.title('Expected Minimum Information vs n')
plt.legend()
plot_filename = 'expected_min_info_extended.png'
plt.savefig(plot_filename)
plt.close()

print(f"Plot saved as {plot_filename}")
