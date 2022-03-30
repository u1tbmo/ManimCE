from manim import *
import numpy as np

class Test(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=(-100,100,1),
            y_range=(-100,100,1),
            x_length=16,
            y_length=9
        )

        graph = plane.plot(
            lambda x: np.sin(x)
        )

        plane.add_coordinates()
        self.add(
            plane,graph
        )