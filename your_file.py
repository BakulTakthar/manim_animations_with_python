from manim import *

class InteractiveScene(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.wait(1)
        self.interactive_embed()