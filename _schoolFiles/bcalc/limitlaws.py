from manim import *
import numpy as np

class LimitLaws(Scene):
    def construct(self):

        law1 = Tex("1: The limit of a constant is itself")
        law1A = MathTex(r"{ \lim_{x\to c} } {k} = {k}")
        law1B = MathTex(r"{ \lim_{x\to c} } {2} = {2}").next_to(law1A, DOWN)
        law1ex = VGroup(law1A, law1B).arrange(DOWN)
        law1name = Tex("The Constant Law")

        law2 = Tex("2: The limit of $x$ as $x$ approaches $c$ is equal to $c$")
        law2A = MathTex(r"{ \lim_{x\to c} } {x} = {c}")
        law2B = MathTex(r"{ \lim_{x\to 2} } {x} = {2}")
        law2ex = VGroup(law2A, law2B).arrange(DOWN)
        law2name = Tex("The Special Limit")

        law3 = Tex("3: The limit of a constant $k$ times a function is equal to the product of that constant and its function's limit").scale(0.7)
        law3A = MathTex(r"{ \lim_{x\to c} } {k} \cdot {f(x)} = k \cdot { \lim_{x\to c} } {f(x)} = k \cdot L")
        law3B = MathTex(r"{ \lim_{x\to c} } {3} \cdot {f(x)} = 3 \cdot { \lim_{x\to c} } {f(x)}")
        law3ex = VGroup(law3A, law3B).arrange(DOWN)
        law3name = Tex("Constant Multiple Theorem")

        law4 = Tex("4: The limit of a sum of functions is the sum of the limits of the individual functions").scale(0.7)
        law4A = MathTex(r"{ \lim_{x\to c} } {(f(x) + g(x))} = { \lim_{x\to c} } {f(x)} + { \lim_{x\to c} } {g(x)} = L + M")
        law4name = Tex("The Addition Theorem / Sum Law")

        law5 = Tex("5: The limit of a difference of functions is the difference of the limits of the individual functions").scale(0.7)
        law5A = MathTex(r"{ \lim_{x\to c} } {(f(x) - g(x))} = { \lim_{x\to c} } {f(x)} - { \lim_{x\to c} } {g(x)} = L - M")
        law5name = Tex("The Subtraction Theorem / Difference Law")

        law6 = Tex("6: The limit of a product of functions is the product of the limits of the individual functions").scale(0.7)
        law6A = MathTex(r"{ \lim_{x\to c} } {(f(x) \cdot g(x))} = { \lim_{x\to c} } {f(x)} \cdot { \lim_{x\to c} } {g(x)} = L \cdot M")
        law6name = Tex("The Multiplication Theorem / Product Law")

        law7 = Tex("7: The limit of a quotient of functions is the quotient of the limits of the individual functions").scale(0.7)
        law7A = MathTex(r"{ \lim_{x\to c} } {\frac{f(x)}{g(x)}} = \frac{\lim_{x\to c}{f(x)}}{\lim_{x\to c}{g(x)}} = \frac{L}{M}, M\neq 0")
        law7name = Tex("The Division Theorem / Quotient Law")

        law8 = Tex("8: The limit of an integer power $p$ of a function is just that power to the limit of the function").scale(0.7)
        law8A = MathTex(r"{ \lim_{x\to c} {(f(x))}^{p}} = ({ \lim_{x\to c}{f(x)} })^{p} = L^{p}")
        law8name = Tex("The Power Law")

        law9 = Tex("9: The limit of the $n$th root of a function is just the $n$th root of the limit of the function, provided that $n$ is positive and real").scale(0.65)
        law9A = MathTex(r"{ \lim_{x\to c} } {\sqrt[n]{f(x)}} = {\sqrt[n]{\lim_{x\to c}{f(x)}}} = \sqrt[n]{L}")
        law9name = Tex("The Radical/Root Law")

        self.play(Write(law1.to_edge(UP)), Write(law1name.to_edge(DOWN)), run_time=1.5)
        self.wait()
        self.play(Write(law1ex, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law1), FadeOut(law1ex), FadeOut(law1name))
        self.wait(1)

        self.play(Write(law2.to_edge(UP)), Write(law2name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law2ex, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law2), FadeOut(law2ex), FadeOut(law2name))
        self.wait(1)

        self.play(Write(law3.to_edge(UP)), Write(law3name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law3ex, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law3), FadeOut(law3ex), FadeOut(law3name))
        self.wait(1)

        self.play(Write(law4.to_edge(UP)), Write(law4name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law4A, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law4), FadeOut(law4A), FadeOut(law4name))
        self.wait(1)

        self.play(Write(law5.to_edge(UP)), Write(law5name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law5A, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law5), FadeOut(law5A), FadeOut(law5name))
        self.wait(1)

        self.play(Write(law6.to_edge(UP)), Write(law6name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law6A, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law6), FadeOut(law6A), FadeOut(law6name))
        self.wait(1)

        self.play(Write(law7.to_edge(UP)), Write(law7name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law7A, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law7), FadeOut(law7A), FadeOut(law7name))
        self.wait(1)

        self.play(Write(law8.to_edge(UP)), Write(law8name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law8A, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law8), FadeOut(law8A), FadeOut(law8name))
        self.wait(1)

        self.play(Write(law9.to_edge(UP)), Write(law9name.to_edge(DOWN)),run_time=1.5)
        self.wait()
        self.play(Write(law9A, run_time=1.5))
        self.wait(3)
        self.play(FadeOut(law9), FadeOut(law9A), FadeOut(law9name))
        self.wait(3)