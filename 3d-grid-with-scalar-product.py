from manim import *
import numpy as np

"""
TODO
!get the animations to work for the video
!add tet to explain and show the calculation
!make the axis bigger
!display coordinates (if good)
!make the paralleopiped and show its volume with animations
"""
# To enable OpenGL rendering:
config.renderer = "opengl"

class ThreeDGridWithLabels(ThreeDScene):
    def construct(self):
        #? making the vectors
        
        vector_a = Arrow(start=ORIGIN, end=[-1,1,0], buff=0, color=YELLOW)
        vector_b = Arrow(start=ORIGIN, end=[-1,1,2], buff=0, color=YELLOW)
        vector_c = Arrow(start=ORIGIN, end=[-2,0,0], buff=0, color=YELLOW)
        
        #? declraing vector d 
        vector_d = Arrow(start=ORIGIN, end=np.cross(np.array(vector_a.end), np.array(vector_c.end)), buff=0, color=RED)
        vector_d.set_stroke(width=7)   
        
        #? making the labels
        label_a = MathTex(r"\overrightarrow{a}").move_to(vector_a.end+[0, 0, 0.2]).rotate(PI/2, axis=RIGHT).rotate(PI, axis=IN)
        label_b = MathTex(r"\overrightarrow{b}").move_to(vector_b.end+[0, 0, 0.2]).rotate(PI/2, axis=RIGHT).rotate(PI, axis=IN)
        label_c = MathTex(r"\overrightarrow{c}").move_to(vector_c.end+[0, 0, 0.2]).rotate(PI/2, axis=RIGHT).rotate(PI, axis=IN)
        label_d = MathTex(r"\overrightarrow{d}").move_to(vector_d.end+[-0.2, 0.2, 0.2]).rotate(PI/2, axis=RIGHT).rotate(PI, axis=IN)
        label_d.set_color(RED)
        #? adding them to the render    
        
        self.add(vector_a, vector_b, vector_c)
        self.add(label_a, label_b, label_c)
        self.wait(2)
        self.add(vector_d, label_d)
        
        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],  # Range for x-axis
            y_range=[-5, 5, 1],  # Range for y-axis
            z_range=[-5, 5, 1],  # Range for z-axis
            x_length=10,         # Length of the x-axis
            y_length=10,         # Length of the y-axis
            z_length=10,         # Length of the z-axis
        )

        # Create grid lines for x-y, y-z, and x-z planes
        x_y_grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"stroke_color": WHITE},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
        )

        # Rotate and place grid for the other planes
        y_z_grid = x_y_grid.copy().rotate_about_origin(PI / 2, axis=RIGHT)
        x_z_grid = x_y_grid.copy().rotate_about_origin(PI / 2, axis=UP)

        # Create labels for x, y, z axes
        x_label = MathTex("x").move_to(axes.c2p(5, 0, 0) + np.array([0.3, 0, 0]))  # Slight offset for x-axis
        y_label = MathTex("y").move_to(axes.c2p(0, 5, 0) + np.array([0, 0.3, 0]))  # Slight offset for y-axis
        z_label = MathTex("z").move_to(axes.c2p(0, 0, 5) + np.array([0, 0, 0.3]))  # Slight offset for z-axis

        # Set the camera angle to view the 3D scene clearly
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Add the 3D axes, grid planes, and axis labels
        self.add(axes, x_y_grid, y_z_grid, x_z_grid, x_label, y_label, z_label)

        self.wait()

        self.interactive_embed()