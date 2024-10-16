from manim import *
import numpy as np

class LorenzAttractor(ThreeDScene):
    def lorenz(self, position, sigma=10, rho=28, beta=8/3):
        """
        Compute the Lorenz system derivatives.
        position: [x, y, z]
        returns: [dx/dt, dy/dt, dz/dt]
        """
        x, y, z = position
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        return np.array([dx, dy, dz])

    def get_lorenz_trajectory(self, start_point, num_steps=5000, dt=0.01):
        """
        Generate the Lorenz trajectory starting from the given point.
        start_point: initial position in [x, y, z]
        returns: array of points for the trajectory
        """
        trajectory = [start_point]
        for _ in range(num_steps):
            current_pos = trajectory[-1]
            new_pos = current_pos + dt * self.lorenz(current_pos)
            trajectory.append(new_pos)
        return np.array(trajectory)

    def construct(self):
        # Set up the 3D axes
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)

        # Initial condition and generate the Lorenz trajectory
        start_point = np.array([1.0, 1.0, 1.0])
        trajectory_points = self.get_lorenz_trajectory(start_point)

        # Create the Lorenz attractor path using a series of small lines
        trajectory_curve = VGroup()  # VGroup to hold the curve as a series of lines
        points = trajectory_points * 0.05  # Scaling down for visualization

        for i in range(len(points) - 1):
            segment = Line(points[i], points[i+1], color=RED, stroke_width=1)
            trajectory_curve.add(segment)

        # Add and animate the Lorenz attractor trajectory
        self.add(trajectory_curve)
        self.begin_ambient_camera_rotation(rate=0.1)  # Rotate camera slowly
        self.play(Create(trajectory_curve), run_time=8, rate_func=linear)
        self.wait()

        