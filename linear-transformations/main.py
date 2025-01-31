from manim import *

class MatrixTransformations(Scene):
    def construct(self):
        # Create a square object

        plane = NumberPlane(x_range=(-5, 5), 
                            y_range=(-5, 5),
                            axis_config={"stroke_color": BLACK},
                            background_line_style={
                                "stroke_color": BLUE_D,
                                "stroke_width": 1,
                                "stroke_opacity": 0.6,
                            },)
        
        plane_transform = NumberPlane(x_range=(-5, 5), 
                            y_range=(-5, 5),
                            axis_config={"stroke_color": BLACK},
                            background_line_style={
                                "stroke_color": BLUE_D,
                                "stroke_width": 1,
                                "stroke_opacity": 0.6,
                            },).set_color(RED)
        

        # Display the original square
        self.play(Create(plane))
        self.wait(1)
        self.play(Write(plane_transform))
        # Define a function to apply matrix transformation
        def apply_custom_matrix_transformation(matrix):
            self.play(ApplyMatrix(matrix, plane_transform), run_time=2)
            

            # Reset the square
            

        # Example matrices: you can change these matrices
        scaling_matrix = [[2, 0], [0, 2]]  # Scaling by a factor of 2
        rotation_matrix = [[0, -1], [1, 0]]  # 90 degree rotation (counter-clockwise)
        shearing_matrix = [[1, 1], [0, 1]]  # Shearing transformation

        # Call the transformation function with any of the matrices
        apply_custom_matrix_transformation(scaling_matrix)
        # apply_custom_matrix_transformation(rotation_matrix)
        # apply_custom_matrix_transformation(shearing_matrix)

        # You can also define your own custom matrix and pass it
        custom_matrix = [[1, 1], [0, -1]]  # Example custom matrix (reflection)
        # apply_custom_matrix_transformation(custom_matrix)
        self.interactive_embed()
