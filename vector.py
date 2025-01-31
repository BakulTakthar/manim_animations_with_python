from manim import *

class Vector3DScene(ThreeDScene):
    def construct(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=7,
            y_length=7,
            z_length=7,
        )

        # Add labels for axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Define the vector
        vector = Vector([2, 3, 1], color=YELLOW)

        # Add vector to the axes
        vector_label = MathTex("\\vec{v} = (2, 3, 1)").next_to(vector, RIGHT)

        # Add camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add all elements to the scene
        self.add(axes, axes_labels, vector, vector_label)
        self.wait()

        self.interactive_embed()