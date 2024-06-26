import random
from manim import *
from matplotlib.backend_bases import RendererBase
import sympy

# Define the symbols
x, y, z = sympy.symbols('x y z')

class Equation(Scene):
    def construct(self):
        # Generate a random equation
        equation = x + y + z + random.randint(-10, 10)
        equation_tex = "$" + latex(equation) + "$"
        equation_mob = Tex(equation_tex)

        # Define the algebraic transformations
        transformations = [
            ("Add", sympy.Add),
            ("Mul", sympy.Mul),
            ("Pow", sympy.Pow),
            ("sin", sympy.sin),
            ("cos", sympy.cos),
            ("exp", sympy.exp)
        ]

        # Animate the equation and transformations
        self.play(Write(equation_mob))
        while True:
            # Generate a random transformation
            name, transformation = random.choice(transformations)
            args = [random.choice([x, y, z, random.randint(-10, 10)]) for _ in range(transformation.__new__(transformation).nargs)]
            new_equation = transformation(*args)
            new_equation_tex = "$" + latex(new_equation) + "$"
            new_equation_mob = Tex(new_equation_tex)

            # Animate the transformation
            self.play(Transform(equation_mob, new_equation_mob))

            # Update the equation
            equation = new_equation
            equation_tex = new_equation_tex

# Create the animation
animation = AnimationGroup(Equation())
renderer = RendererBase(animation)
renderer.run()
