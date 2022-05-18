from manim import *
import numpy as np

class slopeOfATangent(Scene):
    def construct(self):
        xVal = ValueTracker(-4)

        numberPlane = Axes(
            x_length=10,
            y_length=6,
            ).to_edge(DOWN)

        #numberPlane = Axes(
        #    x_length=10,
        #    y_length=6,
        #    x_range=[-4,4, 1],
        #    y_range=[-2,16,2]
        #    ).to_edge(DOWN)


        function = numberPlane.plot(lambda x: np.sin(x))

        slope = always_redraw(
            lambda: numberPlane.get_secant_slope_group(
                xVal.get_value(),
                graph=function,
                dx=0.01,
                secant_line_length=4,
                secant_line_color=YELLOW
            )
        )

        point = always_redraw(lambda: Dot().move_to(
            numberPlane.c2p(xVal.get_value(),function.underlying_function(xVal.get_value()))
        ).scale(0.5))

        self.add(numberPlane,function,slope,point)
        self.wait(0.5)
        self.play(xVal.animate.set_value(4), run_time=6, rate_func=there_and_back_with_pause)
        self.wait()