from manim import *

class SchrodingerEquation(Scene):
    def construct(self):
        # Title
        title = Tex("Schrödinger Equation").scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))

        # Introduction
        intro_text = Tex("The Schrödinger equation describes the behavior of quantum particles.").scale(0.8)
        intro_text.next_to(title, DOWN)
        self.play(Write(intro_text))

        # Schrödinger Equation
        equation = MathTex(
            "i\\hbar\\frac{\partial}{\partial t}\\Psi(x, t) = -\\frac{\\hbar^2}{2m}\\frac{\\partial^2}{\partial x^2}\\Psi(x, t) + V(x)\\Psi(x, t)"
        ).scale(0.9)
        equation.next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(equation))

        # Explanation
        explanation = VGroup(
            Text("Where:"),
            MathTex("i = \\text{Imaginary unit}"),
            MathTex("\\hbar = \\text{Reduced Planck constant}"),
            MathTex("\\Psi(x, t) = \\text{Wave function}"),
            MathTex("m = \\text{Particle mass}"),
            MathTex("V(x) = \\text{Potential energy function}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.8).next_to(equation, DOWN, buff=0.5)
        self.play(Write(explanation))

        self.wait(3)
        self.interactive_embed()


'''
-pqh = for high quality video output (1080p 60fps)

-pql = for low quality video output (480p 30fps)

'''