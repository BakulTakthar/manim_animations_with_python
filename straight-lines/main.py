from manim import *
from manim.opengl import *
import numpy as np

config.background_color = "#f5f3ed"
"""

"""


class MainScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        # needs ZoomedScene
        # needs ZoomedScene

        # Define line1 parameters
        a1 = np.array([2, 3, 4])  # Start point
        d1 = np.array([5, 5, 5])  # Direction vector
        lam_min, lam_max = -4, 4 
        
        # a1_v = Arrow3D(ORIGIN,[2, 3, 4])
        # d1_v = Arrow3D(ORIGIN, d1)
        # Range of the parameter lambda

        # a1_vector = Arrow3D(start=np.array([0,0,0]), end=np.array([2,3,4]), resolution=8)
        # defining the parameters of line2
        a2 = np.array([1, 1, 1])
        d2 = np.array([2, 6, 3])
        
        # a2_v = Arrow3D(ORIGIN, a2)
        # d2_v = Arrow3D(ORIGIN, d2)

        d_prependicular = np.cross(d1, d2)
        
        # d_p_v = Arrow3D(ORIGIN, d_prependicular)

        # Use ParametricFunction for a line
        line1 = ParametricFunction(
            lambda t: a1 + t * d1,  # Line equation
            t_range=[lam_min, lam_max],  # Range of the parameter
            color="#fa0102",
        )
        line1.set_stroke(width=5)

        l1_label = MathTex("l_{1} : r_{1}=a_{1}+\lambda d_{1}", color=BLACK).move_to(
            line1
        )
        l1_label.rotate(3 * (PI / 2), IN).rotate(PI / 2, UP).scale(0.5)

        line2 = ParametricFunction(
            lambda t: a2 + t * d2,  # Line equation
            t_range=[lam_min, lam_max],  # Range of the parameter
            color="#fa0102",
        )
        line2.set_stroke(width=5)

        l2_label = MathTex("l_{2} : r_{2}=a_{2}+\lambda d_{2}", color=BLACK).move_to(
            line2
        )
        l2_label.rotate(3 * (PI / 2), IN).rotate(PI / 2, UP).scale(0.5)

        # # Defining the shortest distance line
        #! TODO
        # d_shortest = np.cross(d1, d2)

        A = np.array([d1, -d2, d_prependicular]).T  # Coefficient matrix

        b = a2 - a1

        # Solve the linear system
        lambdas = np.linalg.lstsq(A, b, rcond=None)[0]
        lam1, lam2 = lambdas[0], lambdas[1]

        p1 = a1 + lam1 * d1  # Closest point on Line 1
        p2 = a2 + lam2 * d2  # Closest point on Line 2
        p0 = (p1 + p2) / 2
        
        p0_label = MathTex('P_{0}', color=BLACK)
        p0_dot = Dot3D(p0, radius=0.1, color = BLACK)
        # diff = a1 - a2
        # lambda_val = np.dot(diff, d_shortest) / np.linalg.norm(d_shortest)**2
        # p_shortest = a1 - lambda_val * d_shortest

        # shortest_line = ParametricFunction(
        #     lambda u: p_shortest + u * d_shortest,
        #     t_range=[-1, 1],  # Adjust this range for the line
        #     color=RED
        # )

        # point_1_d = np.intersect1d(line1.points, shortest_line.points)
        # point_2_d = np.intersect1d(line2.points, shortest_line.points)
        line3 = ParametricFunction(
            lambda t: (p0) + t * d_prependicular,  # Line equation
            t_range=[lam_min, lam_max],  # Range of the parameter
            color="#284283",
        )
        line3.set_stroke(width=5)
        # # short_dist = Line3D(point_1_d, point_2_d, 0.8, BLUE)

        # shortest_distance_line = Line3D(p1, p2, color=YELLOW)

        p1_point = Dot3D(p1, color=BLACK)
        p2_point = Dot3D(p2, color=BLACK)

        p2_label = MathTex("P_{2}").move_to(p2)

        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=10,
            color= BLACK
        )
        axes.set_color(BLACK)

        # Create grid lines for x-y, y-z, and x-z planes
        x_y_grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"stroke_color": BLACK},
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6,
            },
        )

        # Rotate and place grid for other planes
        y_z_grid = x_y_grid.copy().rotate_about_origin(PI / 2, axis=RIGHT)
        x_z_grid = x_y_grid.copy().rotate_about_origin(PI / 2, axis=UP)

        # Create labels for x, y, z axes
        x_label = (
            MathTex("x", color = BLACK)
            .move_to(axes.c2p(5, 0, 0) + np.array([0.3, 0, 0]))
            .rotate(3 * PI / 2, LEFT)
        )
        y_label = (
            MathTex("y", color = BLACK)
            .move_to(axes.c2p(0, 5, 0) + np.array([0, 0.3, 0]))
            .rotate(3 * PI / 2, LEFT)
        )
        z_label = (
            MathTex("z", color = BLACK)
            .move_to(axes.c2p(0, 0, 5) + np.array([0, 0, 0.3]))
            .rotate(3 * PI / 2, LEFT)
        )
        l1_label.move_to(line1)

        # Add everything to the scene
        # self.add(
        #     x_y_grid,
        #     y_z_grid,
        #     x_z_grid,
        #     axes,
        #     x_label.set_color(BLACK),
        #     y_label.set_color(BLACK),
        #     z_label.set_color(BLACK),
        #     line1,
        #     line2,
        #     line3,
        # )
        # self.add(p1_point, p2_point, l1_label, l2_label)
        
        self.wait(5)

        self.play(
            Create(axes),
            Create(x_y_grid),
            Create(y_z_grid),
            Create(x_z_grid),
            Create(x_label),
            Create(y_label),
            Create(z_label),
            Create(line1),
            Write(l1_label)
        )
        self.add(line1)
        
        self.wait(2)
        
        self.play(Create(line2),
            Write(l2_label))
        self.add(line2)
        
        
        self.wait(2)
        
        self.play(Create(line3))
        self.add(line3)
        
        self.wait(2)
        
        self.play(Create(p1_point),Create(p2_point))
        # Animate the line

        # self.play(Create(shortest_line))
        # self.play(Create(short_dist))
        self.wait(5)
        self.interactive_embed()

# scene = MainScene()