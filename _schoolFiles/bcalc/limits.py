from manim import *
import numpy as np

class Limits(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-8,8,1],y_range=[-4.5,4.5,1],
        background_line_style=
        {
            "stroke_opacity":0.4
        }
        )
        plane.add_coordinates()
        graph = plane.plot(lambda x: np.divide(x-1,x-1),color=YELLOW)
        label = MathTex(r"f(x)=\frac{x-1}{x-1}")
        point = Dot().move_to(plane.coords_to_point(1,1)).scale(0.75)
        pointLabel = MathTex("P").next_to(point,UP).scale(0.75)

        prompt1 = Tex(r'If $x=1$ then P is undefined').to_corner(UP+RIGHT)
        prompt2 = Tex(r'Find $\lim_{x\to 1}{ f(x) }$').to_corner(DOWN+RIGHT)

        self.play(FadeIn(plane),run_time=0.5)
        self.wait(0.1)
        self.play(Write(graph),run_time=2)
        self.wait(0.5)
        self.play(Write(label.to_corner(DOWN+LEFT)))
        self.wait(1)
        self.play(FadeIn(point))
        self.wait(0.5)
        self.play(FadeIn(pointLabel))
        self.wait(1)
        self.play(FadeIn(prompt1))
        self.wait(1)
        self.play(FadeIn(prompt2))
        self.wait(1)

class Limits3(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-16,16,1],y_range=[-8,8,1],
        background_line_style=
        {
            "stroke_opacity":0.4
        }
        ).scale(0.75)

        dfunction = lambda x: np.divide(np.power(x,2)-5,x-2)
        #lfunction = lambda x: x - 2 = 0
        plane.add_coordinates()
        #function = ParametricFunction(self.function,color=YELLOW,discontinuities=[1,3])
        graph = plane.plot(dfunction,discontinuities=[2],dt=0.1,color=YELLOW)
        #line = plane.plot(lfunction,color=GREEN)
        line = Line(plane.coords_to_point(2,7),plane.coords_to_point(2,-7),color=GREEN)
        label = MathTex(r"f(x)=\frac{x^{2}-5}{x-2}")
        prompt = Tex(r'As $x$ approaches 2, there are two different values').scale(0.5)
        prompt2 = Tex(r'therefore the limit does not exist').scale(0.5)

        self.play(FadeIn(plane),run_time=0.5)
        self.wait(0.1)
        self.play(Write(graph),run_time=2)
        self.wait(0.5)
        self.play(Write(line),run_time=1)
        self.wait(0.5)
        self.play(Write(label.to_corner(UP+LEFT)))
        self.wait(1)
        self.play(Write(prompt.next_to(label,DOWN).shift(RIGHT*0.8)))
        self.wait(0.5)
        self.play(Write(prompt2.next_to(prompt,DOWN)))
        self.wait(2)