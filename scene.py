from manim import *

class BernoullisTheorem(Scene):
    def construct(self):
        # Title
        title = Text("Bernoulli's Theorem", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # Equations
        equation1 = MathTex(
            "P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2"
        )
        equation1.next_to(title, DOWN, buff=1)
        equation2 = MathTex(
            "P + \\frac{1}{2}\\rho v^2 + \\rho gh = \\text{Constant}"
        )
        equation2.next_to(equation1, DOWN, buff=0.5)

        self.play(Write(equation1))
        self.play(Write(equation2))
        self.wait(2)

        # Concept
        concept_text = Text(
            "Bernoulli's theorem relates the pressure, velocity, \n and elevation along a streamline in a fluid flow.",
            font_size=24,
            color=BLUE
        )
        concept_text.to_corner(DL)
        self.play(Write(concept_text))
        self.wait(2)

        # Key Idea
        key_idea_text = Text(
            "It states that the total mechanical energy per unit mass of the fluid remains constant.",
            font_size=24,
            color=GREEN
        )
        key_idea_text.to_corner(DL)
        self.play(Transform(concept_text, key_idea_text))
        self.wait(2)

        # Example
        example_text = Text(
            "For example, consider a fluid flowing through a pipe of varying diameter.",
            font_size=24,
            color=ORANGE
        )
        example_text.to_corner(DL)
        self.play(Transform(concept_text, example_text))
        self.wait(2)

        # Animation End
        self.play(FadeOut(title), FadeOut(equation1), FadeOut(equation2), FadeOut(concept_text))
        self.wait(1)
