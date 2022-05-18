from manim import *
import numpy as np
import text as t

class boxVolume(Scene):
    def construct(self):
        xV = ValueTracker(0)
        
        ax = Axes(
            x_length=7, y_length=5, x_range=[-0.2,8,1], y_range=[-20, 530, 80]
        ).to_edge(RIGHT)

        func = ax.plot(lambda x: (25-2*x)*(15-2*x)*(x), color=PINK)
        
        funcLabel = MathTex("V(x) = (25-2x)(15-2x)(x)", color=WHITE)
        funcLabel.next_to(func, UP, buff=0.5)

        volumeLabel = always_redraw(
            lambda: Text(
                'V(' + str(round(xV.get_value(),3)) + ') = ' + str(round(func.underlying_function(xV.get_value()),2)), font='CMU Serif'
                ).to_edge(LEFT, buff=1).scale(0.8)
            )

        funcprime = ax.plot(lambda x: (12*x**2) - (160*x) + (375), color=BLUE)
        funcprimeLabel = Text("V'(3.034) = 0", font='CMU Serif')
        funcprimeLabel.next_to(volumeLabel, DOWN, buff=0.5).shift(RIGHT*0.4).scale(0.8)

        tanLine = always_redraw(
            lambda: ax.get_secant_slope_group(
                xV.get_value(),
                graph=func,
                dx=0.01,
                secant_line_length=2,
                secant_line_color=GREEN
            )
        )
        point = always_redraw(
            lambda: Dot(color=WHITE).move_to(
                ax.c2p(
                    xV.get_value(),
                    func.underlying_function(xV.get_value())
                )
            ).scale(0.8)
        )
        dfpoint = always_redraw(
            lambda: Dot(color=WHITE).move_to(
                ax.c2p(
                    xV.get_value(),
                    funcprime.underlying_function(xV.get_value())
                )
            ).scale(0.8)
        )

        self.play(FadeIn(ax, func, funcprime ,tanLine, point, dfpoint, funcLabel, volumeLabel))
        self.wait(1)
        self.play(xV.animate.set_value(7.5), run_time=6, rate_func=there_and_back)
        self.wait(1)
        self.play(xV.animate.set_value(3.03425), run_time=5)
        self.wait(1)
        self.play(Write(funcprimeLabel))
        self.wait(2)

class details(Scene):
    def construct(self):
        # Set Image Directory
        imageDir = "D:\School Files\Grade 11 - Section P - SY 2021-2022\Basic Calculus\\4thQuarter\PT-Pics"
        
        # Word Problem
        problemHeader = Text(t.problemHeader, font='CMU Serif')
        problem = Text(t.problem, font='CMU Serif', font_size=24)

        # Text Headers of Images
        b1t = Text(t.b1t, font='CMU Serif').to_edge(UP).scale(0.8)
        b2t = Text(t.b2t, font='CMU Serif').to_edge(UP).scale(0.8)
        b3t = Text(t.b3t, font='CMU Serif').to_edge(UP).scale(0.8)
        at = Text(t.at, font='CMU Serif').to_edge(UP).scale(0.8)

        # Image of Box and Diagram
        b1 = ImageMobject(f"{imageDir}\\Before1.png").scale(0.75).to_edge(DOWN)
        b2 = ImageMobject(f"{imageDir}\\Before2.png").scale(0.75).to_edge(DOWN)
        b3 = ImageMobject(f"{imageDir}\\Before3.png").scale(0.75).to_edge(DOWN)
        a = ImageMobject(f"{imageDir}\\After.png").scale(0.75).to_edge(DOWN)

        # Rendering
        self.next_section("Problem")
        self.play(Write(problemHeader))
        self.wait()
        self.play(problemHeader.animate.to_edge(UP))
        self.wait()
        self.play(Write(problem))
        self.wait(3)
        self.play(FadeOut(problemHeader), FadeOut(problem))
        self.wait(3)

        self.next_section("Images")
        self.play(FadeIn(b1t, b1))
        self.wait(2)
        self.play(FadeOut(b1t, b1), FadeIn(b2t, b2))
        self.wait(2)
        self.play(FadeOut(b2t, b2), FadeIn(b3t, b3))
        self.wait(2)
        self.play(FadeOut(b3t, b3), FadeIn(at, a))
        self.wait(2)
        self.play(FadeOut(at, a))
        self.wait(3)