from manim import *
import random

class MathAnimations(Scene):
    def construct(self):
        # Create a text object
        text = Text("Random Math Animations").scale(2)
        self.play(Write(text))

        # Create and animate a random equation
        eq1 = MathTex("f(x)=", random.choice(["\\sin", "\\cos", "\\tan"]),"(", "ax^2", "+", "bx", "+", "c", ")")
        eq1.next_to(text, DOWN)
        self.play(Write(eq1))

        # Create and animate a random fraction
        frac = MathTex("\\frac{", random.choice(["x", "y", "z"])," + ", str(random.randint(1, 10)), "}{", random.choice(["a", "b", "c"])," - ", str(random.randint(1, 10)), "}")
        frac.next_to(eq1, DOWN)
        self.play(Write(frac))

        # Create and animate a random integral
        integral = MathTex("\\int_", "0", "^", "1", random.choice(["x", "y", "z"]), "^2", "d", random.choice(["x", "y", "z"]))
        integral.next_to(frac, DOWN)
        self.play(Write(integral))

        # Create and animate a random matrix
        matrix = Matrix([[random.randint(1, 10) for j in range(3)] for i in range(3)])
        matrix.next_to(integral, DOWN)
        self.play(Write(matrix))

        # Create and animate a random summation
        summation = MathTex("\\sum_{", random.choice(["i", "j", "k"]), "=", "1}^", str(random.randint(1, 10)), random.choice(["x", "y", "z"]), "_", str(random.randint(1, 10)))
        summation.next_to(matrix, DOWN)
        self.play(Write(summation))

        # Wait for the animations to complete
        self.wait()

        # Save the animation as a GIF file
        self.render(output_file='math_animations.gif')

if __name__ == '__main__':
    scene = MathAnimations()
    scene.render(
        
       
    )