from manim import *

class SineWaveSurfaceLarge(ThreeDScene):
    def construct(self):
        # Set up larger axes
        axes = ThreeDAxes(
            x_range=[-10, 10, 2],
            y_range=[-10, 10, 2],
            z_range=[-5, 5, 1],
            x_length=100,
            y_length=100,
            z_length=70,
        )
        
        # Create the sine wave surface with larger range
        sine_wave = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(np.sqrt(u**2 + v**2))
            ]),
            u_range=[-10, 10],
            v_range=[-10, 10],
            resolution=(50, 50),  # Increase resolution for smoothness
            fill_opacity=0.8,
            checkerboard_colors=[BLUE, GREEN],
        )
        
        # Add axes and surface to the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes, sine_wave)
        
        # Rotate the camera to show the surface from different angles
        self.begin_ambient_camera_rotation(rate=0.2)
        self.stop_ambient_camera_rotation()
        self.wait(10)
        self.interactive_embed()
