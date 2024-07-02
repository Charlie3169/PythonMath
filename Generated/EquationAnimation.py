from manim import *
import random

class EquationAnimation(Animation):
    def __init__(self, equation, **kwargs):
        super().__init__(equation, **kwargs)
        self.equation = equation
    
    def interpolate_mobject(self, alpha):
        # Perform some random algebraic transformations on the equation
        new_equation = self.equation.copy()
        num_transforms = random.randint(1, 3)
        for i in range(num_transforms):
            transformation = random.choice(["expand", "factor", "simplify"])
            if transformation == "expand":
                new_equation = new_equation.expand()
            elif transformation == "factor":
                new_equation = new_equation.factor()
            else:
                new_equation = new_equation.simplify()
        self.mobject.become(Tex(new_equation))

class EquationScene(Scene):
    def construct(self):
        equation = Tex("x^2 + 2x + 1 = 0")
        self.play(Create(equation))
        self.wait(1)

        animation = EquationAnimation(equation)
        self.play(animation)
        self.wait(1)
