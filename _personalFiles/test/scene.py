from calendar import c
from cmath import sin
from manim import *

class Test1(Scene):
    def construct(self):
        blueCircle = Circle(color=BLUE, fill_opacity=0.5)
        greenSquare = Square(color=GREEN, fill_opacity=0.5)
        yellowTriangle = Triangle(color=YELLOW,fill_opacity=0.5)
        greenSquare.next_to(blueCircle, RIGHT)
        yellowTriangle.next_to(blueCircle,LEFT)
        
        self.play(Create(blueCircle))
        self.wait()
        self.play(Create(greenSquare))
        self.wait()
        self.play(Create(yellowTriangle))
        self.wait(2)

class Test2(Scene):
    def construct(self):
        ax =  Axes(x_range=[-5,5],y_range=[-3,3])
        curve = ax.plot(lambda x:(x+2)*x*(x-2), color=RED)
        area = ax.get_area(curve, x_range=[-2,0])
        self.play(Create(ax))
        self.wait()
        self.play(Create(curve, run_time=1.5))
        self.wait()
        self.play(FadeIn(area))
        self.wait(2)