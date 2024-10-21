from manim import *

# To enable OpenGL rendering:
config.renderer = "opengl"

class OpenGLSurfaceExample(ThreeDScene):
    def construct(self):
        # Setting up the axes for the 3D scene
        axes = ThreeDAxes()

        # Define the surface using a lambda function for parametric surface
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-3, 3],  # range for u
            v_range=[-3, 3],  # range for v
            resolution=(30, 30),
        )

        # Set surface style and color
        surface.set_style(fill_opacity=0.8, fill_color=BLUE)
        surface.set_fill_by_value(axes=axes, colors=[BLUE, GREEN, YELLOW])

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add(axes, surface)

        self.wait()

        self.interactive_embed()