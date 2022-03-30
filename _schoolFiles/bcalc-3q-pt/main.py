from manim import *
import numpy as np
import variables as v



class Q1Graphical(Scene):
    def construct(self):

        approachG = Tex("Graphical Approach")

        self.play(Write(approachG))
        self.wait(2)
        self.play(Unwrite(approachG))
        self.wait(0.5)
        
        self.play(Write(v.Ques1))
        self.wait(1.5)

        self.play(FadeOut(v.Ques1Prompt))
        self.wait(0.5)
        self.play(v.Ques1Eq.animate.to_edge(UP+RIGHT))
        self.wait(0.5)

        v.plane1a.add_coordinates()
        self.play(FadeIn(v.plane1a))
        self.wait(1)
        
        self.play(Write(v.graph1a))
        self.wait(1)

        self.play(
            FadeOut(v.plane1a),
            FadeOut(v.graph1a)
        )
        self.wait(0.5)

        v.plane1b.add_coordinates()
        self.play(FadeIn(v.plane1b))
        self.wait(1)
        
        self.play(FadeIn(v.graph1b))
        self.wait(1)

        self.play(
            Write(v.line1bX),
            Write(v.line1bY)
        )
        self.wait(1.5)

        self.play(
            Write(v.point1b),
            Write(v.point1bLabel)
        )
        self.wait(0.5)

        self.play(
            FadeOut(v.line1bX),
            FadeOut(v.line1bY)
        )
        self.wait(2)

        self.play(
            FadeOut(v.plane1b),
            FadeOut(v.graph1b),
            FadeOut(v.point1b),
            FadeOut(v.point1bLabel),
            FadeOut(v.Ques1Eq)
            )
        self.wait(0.5)

        self.play(
            Write(v.label1)
        )
        self.wait(2)

        self.play(Unwrite(v.label1))
        self.wait()

class Q2Graphical(Scene):
    def construct(self):

        approachG = Tex("Graphical Approach")

        self.play(Write(approachG))
        self.wait(2)
        self.play(Unwrite(approachG))
        self.wait(0.5)

        self.play(Write(v.Ques2))
        self.wait(1.5)

        self.play(FadeOut(v.Ques2Prompt))
        self.wait(0.5)
        self.play(v.Ques2Eq.animate.to_edge(UP+LEFT))
        self.wait(0.5)
        
        self.play(Write(v.Given))
        self.wait(1.5)

        self.play(v.Given.animate.next_to(v.Ques2Eq,DOWN))
        self.wait(0.5)

        self.play(Write(v.Ques2EqCopy))
        self.wait(1)

        self.play(ReplacementTransform(v.Ques2EqCopy,v.Ques2FinalEq))
        self.wait(0.5)

        self.play(ReplacementTransform(
            v.Ques2FinalEq,v.Ques2FinalEqCopy.scale(0.6).to_edge(UP+RIGHT)),
            FadeOut(v.Ques2Eq),
            FadeOut(v.Given)
        )
        self.wait(1.5)

        v.plane2a.add_coordinates()
        self.play(FadeIn(v.plane2a))
        self.wait(1)
        
        self.play(Write(v.graph2a))
        self.wait(2)

        self.play(
            FadeOut(v.plane2a),
            FadeOut(v.graph2a)
        )
        self.wait(0.5)

        v.plane2b.add_coordinates()
        self.play(Write(v.plane2b))
        self.wait(1)

        self.play(FadeIn(v.graph2b))
        self.wait(1)

        self.play(
            Write(v.line2bX),
            Write(v.line2bY)
            )
        self.wait(1.5)

        self.play(
            Write(v.point2b),
            Write(v.point2bLabel)
        )
        self.wait(0.5)

        self.play(
            FadeOut(v.line2bX),
            FadeOut(v.line2bY),
        )
        self.wait(2)

        self.play(
            FadeOut(v.plane2b),
            FadeOut(v.graph2b),
            FadeOut(v.point2b),
            FadeOut(v.point2bLabel),
            FadeOut(v.Ques2FinalEqCopy),
        )
        self.wait(0.5)
        
        self.play(Write(v.label2))
        self.wait(2)
        
        self.play(Unwrite(v.label2))
        self.wait()