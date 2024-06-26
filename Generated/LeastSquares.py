import numpy as np
import matplotlib.pyplot as plt
import imageio

# Set up random seed for reproducibility
np.random.seed(42)

# Set up dataset
x = np.linspace(-10, 10, 20)
y = 2 * x + 3 + np.random.normal(0, 5, len(x))

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-50, 50)
line, = ax.plot([], [], 'r', label='Best Fit Line')
ax.legend()
points = ax.scatter([], [])

# Define function to calculate best fit line
def best_fit_line(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, b

# Define function to calculate distance from point to line
def point_to_line_distance(x, y, m, b):
    return abs((y - m * x - b) / np.sqrt(1 + m ** 2))

# Set up writer for saving animation as GIF
writer = imageio.get_writer('best_fit_line.gif', fps=2)

# Add points to dataset one at a time and update plot
for i in range(len(x)):
    # Update dataset
    new_x = x[:i+1]
    new_y = y[:i+1]
    
    # Calculate best fit line for updated dataset
    m, b = best_fit_line(new_x, new_y)
    
    # Calculate distances from each point to best fit line
    distances = point_to_line_distance(new_x, new_y, m, b)
    
    # Update plot with new points and lines
    points.set_offsets(np.c_[new_x, new_y])
    lines = []
    for j in range(len(new_x)):
        lines.append(ax.plot([new_x[j], new_x[j]], [new_y[j], m * new_x[j] + b], 'k--', alpha=0.3)[0])
    
    # Update best fit line
    line.set_data([np.min(new_x), np.max(new_x)], [m * np.min(new_x) + b, m * np.max(new_x) + b])
    
    # Add frame to animation
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    writer.append_data(image)

# Close writer and show plot
writer.close()
plt.show()

