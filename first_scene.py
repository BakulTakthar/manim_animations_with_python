from manim import *
from manim.opengl import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        traingle = Triangle()
        square = Square()
        
        circle.shift(LEFT)
        traingle.shift(RIGHT)
        square.shift(UP)
        
        self.add(circle, traingle, square)
        self.wait(2)
        self.embed()
