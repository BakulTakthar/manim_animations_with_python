from manim import *
import numpy as np

config.background_color = WHITE

class FirstScene(Scene):
    def construct(self):
        
        sphere = Sphere(radius = 0.2, resolution=(24,48))
    
        sphere.set_color("#000080", opacity=1)
        
        sphere_field = Sphere(radius = 1.5, resolution=(24,48))
    
        sphere_field.set_color(PINK, opacity=0.3)
        
        plane = Surface(
            lambda u, v: np.array([u, 0, v]),  # Define the plane as X-Z axis
            u_range=[-2, 2],  # X-axis limits
            v_range=[-2, 2],  # Z-axis limits
        )
        plane.set_color(BLUE, opacity=1)
        
        plane.shift(UP)

        # Rotate the plane to make it vertical
          # Rotate 90° around the X-axis

        # Add the plane to the scene
        self.add(plane)
        
        self.add(sphere)
        self.add(sphere_field)
        
        
        self.interactive_embed()
