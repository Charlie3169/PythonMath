from PIL import Image

# Define the size of the image
width = 600
height = 400

# Define the coordinates of the complex plane
x_min, x_max = -2, 1
y_min, y_max = -1, 1

# Create the image and set its color mode to RGB
image = Image.new("RGB", (width, height))

# Define the maximum number of iterations
max_iterations = 100

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Convert the pixel coordinates to complex numbers
        cx = x_min + (x / width) * (x_max - x_min)
        cy = y_min + (y / height) * (y_max - y_min)
        c = complex(cx, cy)

        # Initialize the iteration count and the value of z
        z = 0
        n = 0

        # Calculate the value of z using the Mandelbrot set formula
        while abs(z) <= 2 and n < max_iterations:
            z = z*z + c
            n += 1

        # Set the color of the pixel based on the number of iterations
        if n == max_iterations:
            color = (0, 0, 0)
        else:
            color = (n % 256, (n*5) % 256, (n*10) % 256)

        # Set the color of the pixel in the image
        image.putpixel((x, y), color)

# Save the image
image.save("mandelbrot.png")
