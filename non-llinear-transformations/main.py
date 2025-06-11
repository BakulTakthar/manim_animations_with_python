from manim import *
import numpy as np

class CustomNonlinearTransform(LinearTransformationScene):
    def setup(self):
        # Create a high-resolution NumberPlane
        self.plane = NumberPlane(
            x_range=[-8, 8, 0.2],
            y_range=[-5, 5, 0.2],
            faded_line_ratio=4,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            resolution=(128, 80)
        )
        self.add(self.plane)
        super().setup()

    def func(self, point):
        x, y, z = point
        return np.array([
            x+ y**3,
            y+ x**3,
            z
        ])
    
    def construct(self):

        
        vectorx = Vector(np.array([1, 0, 0]))  # Example vector to transform
        vectory = Vector(np.array([0, 1, 0]))  # Example trajectory to transform
        # Optional: make grid more detailed
        self.add(vectory, vectorx)
        self.plane.prepare_for_nonlinear_transform()

        self.wait()
        self.apply_nonlinear_transformation(self.func)
        
        self.wait()
        self.interactive_embed()
