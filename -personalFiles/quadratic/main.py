from manim import *

# Scenes

class QuadraticFormula(Scene):
    def constuct(self):
        eq1=MathTex(r'ax^2+bx+c=0')
        eq2=MathTex(r'ax^2+bx=-c')
        eq3=MathTex(r'x^2+{b\over a}x=-{c\over a}')
        eq4=MathTex(r'x^2+{b\over a}x+\left({b\over 2a}\right)^2=-{c\over a}+\left({b\over 2a}\right)^2')
        eq5=MathTex(r'\left(x+{b\over 2a}\right)^2=-{c\over a}+\left({b\over 2a}\right)^2')
        eq6=MathTex(r'\left(x+{b\over 2a}\right)^2=-{c\over a}+{b^2\over 4a^2}')
        eq7=MathTex(r'\left(x+{b\over 2a}\right)^2={b^2\over 4a^2}-{c\over a}')
        eq8=MathTex(r'\left(x+{b\over 2a}\right)^2={b^2\over 4a^2}-{4c\over 4a}')
        eq9=MathTex(r'\left(x+{b\over 2a}\right)^2={b^2\over 4a^2}-{4ac\over 4a^2}')
        eq10=MathTex(r'\left(x+{b\over 2a}\right)^2a={b^2-4ac\over 4a^2}')
        eq11=MathTex(r'\sqrt{\left(x+{b\over 2a}\right)^2}=\pm\sqrt{ {b^2-4ac\over 4a^2} }')
        eq12=MathTex(r'x+{b\over 2a}=\pm\sqrt{ {b^2-4ac\over 4a^2} }')
        eq13=MathTex(r'x=-{b\over 2a}\pm\sqrt{ {b^2-4ac\over 4a^2} }')
        eq14=MathTex(r'x=-{b\over 2a}\pm{\sqrt{b^2-4ac}\over 2a}')
        eq15=MathTex(r'x={-b\pm\sqrt{b^2-4ac}\over 2a}')

        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait()