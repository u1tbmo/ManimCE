from manim import *
import numpy as np

class NumberPlaneBG(Scene):
    def construct (self):
        np = NumberPlane(
            x_range=[1,20,1],
            y_range=[1,20,1],
            faded_line_ratio=3,
            color=ORANGE,
            background_line_style={
                "stroke_color":ORANGE,
                "stroke_opacity": 0.8   
            }
        )

        self.play(Write(np))
        self.wait(2)