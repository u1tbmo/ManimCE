from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        #VARS
        limitsTitle = Text("Real Life Application of Limits",font="CMU Serif").scale(1.25)
        groupName = Tex("Limit of the Brain").scale(1.25)
        chua = Tex("Chua, Arliyah Carmen")
        dayao = Tex("Dayao, Sophia Nicole")
        mariano = Tex("Mariano, Eunice Reign")
        tabamo = Tex("Tabamo, Euan Jed")
        members = VGroup(chua,dayao,mariano,tabamo).arrange(DOWN)


        #SCENES
        self.play(Write(limitsTitle),run_time=4)
        self.wait(2)

        self.play(Unwrite(limitsTitle))
        self.wait(1)

        self.play(Write(groupName),run_time=1.5)
        self.wait(0.5)
        self.play(groupName.animate.to_edge(UP))
        self.wait(1)
        
        self.play(Write(members),run_time=4)
        self.wait(2)

        self.play(
            FadeOut(groupName),
            FadeOut(members),
            run_time = 2
        )
        self.wait(2)

class limitIntro(Scene):
    def construct(self):
        limitExample = MathTex('\\lim_{x\\to c}{f(x)}')
        nplane = NumberPlane(
            x_range=[-14.22,14.22,1],
            y_range=[-8,8,1],
            x_length=14.22,
            y_length=8,
            faded_line_ratio=3,
            color=ORANGE,
            background_line_style={
                "stroke_color":ORANGE,
                "stroke_opacity": 0.4   
            }
        )
        graph = nplane.plot(lambda x: np.divide(x**2+4*x-12,x**2-2*x),discontinuities=[0,2],dt=0.1)
        limOfGraph = MathTex('\\lim_{x\\to2}{ \\frac{x^2+4x-12}{x^2-2x} }').scale(0.75).to_edge(UP+LEFT)
        point = Dot(nplane.c2p(2,4),fill_opacity=0,color=WHITE,stroke_width=2).scale(1)

        self.play(Write(limitExample))
        self.wait(3.5)
        self.play(FadeOut(limitExample))
        self.wait(1)
        self.play(
            FadeIn(nplane),
            Write(limOfGraph)
        )
        self.wait(1)
        self.play(
            Write(graph),
            Write(point)
        )
        self.wait(2)

        self.play(
            FadeOut(nplane),
            FadeOut(limOfGraph),
            FadeOut(graph),
            FadeOut(point)
        )


class Q1Algebraic(Scene):
    def construct(self):
        
        #VARS1
        prob1prompt = Text("Problem 1",font="CMU Serif",font_size=48)
        
        approachA = Tex("Algebraic Approach")

        prob1 = Text("Giselle is an incoming grade 12 student and needs an extra source of income for her sick dog.\nShe is planning to start a small, temporary business selling\nmini pastries made by herand her younger brother, Mark.\nThey are planning to put these up for sale for the next seven days.", font="CMU Serif", font_size=24, line_spacing=1.5)
        
        prob1ques = Tex("How many pastry box sets do Giselle and Mark have to prepare to last all week if the formula of these boxes is:")

        bEq = MathTex(r'b=\frac{x^4}{4^2+2^2+x}')
        
        givenText = Tex("Given:")
        limOfB = MathTex('\\lim_{x\\to7}{\\frac{x^4}{4^2+2^2+x}} \\ ')

        prob1HeaderQues = VGroup(prob1ques,bEq).arrange(DOWN).scale(0.6).to_edge(UP)
        given = VGroup(givenText,limOfB).arrange(DOWN).scale(0.6)

        step1 = limOfB.copy().scale(2)
        step2 = MathTex('=\\frac{ {7}^{4} }{ {4}^{2} + {2}^{2} + {7} }')
        step3 = MathTex('=\\frac{2401}{27}')
        step4 = MathTex('=88.925')
        step5 = MathTex('\\approx 89')
        finalAns = MathTex('\\lim_{x\\to7}{ \\frac{ {x}^{4} }{ {4}^{2}+{2}^{2}+{x} } } \\approx 89 \\ ')

        #SCENES1
        self.play(Write(prob1prompt))
        self.wait(2)
        self.play(prob1prompt.animate.to_edge(UP))
        self.wait(1)

        self.play(Write(prob1),run_time=4)
        self.wait(4)

        self.play(
            FadeOut(prob1),
            FadeOut(prob1prompt)
        )
        self.wait(1)

        self.play(Write(approachA))
        self.wait(2)
        self.play(Unwrite(approachA))
        self.wait(0.5)

        self.play(Write(prob1HeaderQues))
        self.wait(3)

        self.play(FadeOut(prob1HeaderQues))
        self.wait(0.5)

        self.play(
            Write(givenText),
            Write(bEq.next_to(givenText,DOWN))
        )
        self.wait(1)

        self.play(
            ReplacementTransform(bEq,limOfB)
        )
        self.wait(2)

        self.play(given.animate.to_edge(UP+LEFT))
        self.wait(1)

        self.play(Write(step1))
        self.wait(1)
        self.play(ReplacementTransform(step1,step2))
        self.wait(1)
        self.play(ReplacementTransform(step2,step3))
        self.wait(1)
        self.play(ReplacementTransform(step3,step4))
        self.wait(1)
        self.play(ReplacementTransform(step4,step5))
        self.wait(3)

        self.play(
            FadeOut(step5),
            FadeOut(given)
        )
        self.wait()

        self.play(Write(finalAns))
        self.wait(3)
        self.play(Unwrite(finalAns))
        self.wait()

class Q2Algebraic(Scene):
    def construct(self):
        
        #VARS2
        prob2prompt = Text("Problem 2",font="CMU Serif",font_size=48)
        
        approachA = Tex("Algebraic Approach")

        prob2 = Text("Dray recently invested PHP 50,000 in a bank.\nHis savings plan allows the amount to get compounded quarterly at 1.5% annual interest.\nWhat is the future value of Dray’s investment after 7 years?", font="CMU Serif", font_size=24, line_spacing=1.5)
        
        prob2ques = Tex("What is the future value of Dray’s investment after 7 years?")

        FVEq = MathTex('FV(t)=PV(1+\\frac{r}{n})^{nt}')
        
        givenText = Tex("Given:")
        limOfFV = MathTex('\\lim_{t\\to7}{50,000(1+\\frac{0.015}{4})^{4t}}')
        pv = MathTex('PV = 50,000')
        r = MathTex('r = 0.015')
        n = MathTex('n = 4')
        t = MathTex('t = 7')

        prob2HeaderQues = VGroup(prob2ques,FVEq).arrange(DOWN).scale(0.6).to_edge(UP)
        given = VGroup(givenText,limOfFV,pv,r,n,t).arrange(DOWN).scale(0.6)

        step1 = limOfFV.copy().scale(2)
        step2 = MathTex('=50,000(1+\\frac{0.015}{4})^{4\\cdot7}')
        step3 = MathTex('=50,000(1+0.00375)^{28}')
        step4 = MathTex('=50,000(1.00375)^{28}')
        step5 = MathTex('=50,000\\cdot1.1104925057')
        step6 = MathTex('=55,524.625')
        step7 = MathTex('\\approx55,524.63')
        finalAns = MathTex('\\lim_{t\\to7}{PV(1+\\frac{r}{n})^{nt}}=55,524.63')

        #SCENES2
        self.play(Write(prob2prompt))
        self.wait(2)
        self.play(prob2prompt.animate.to_edge(UP))
        self.wait(1)

        self.play(Write(prob2),run_time=4)
        self.wait(4)

        self.play(
            FadeOut(prob2),
            FadeOut(prob2prompt)
        )
        self.wait(1)

        self.play(Write(approachA))
        self.wait(2)
        self.play(Unwrite(approachA))
        self.wait(0.5)

        self.play(Write(prob2HeaderQues))
        self.wait(3)

        self.play(FadeOut(prob2HeaderQues))
        self.wait(0.5)

        self.play(
            Write(givenText),
            Write(FVEq.next_to(givenText,DOWN)),
            Write(pv.next_to(FVEq,DOWN)),
            Write(r.next_to(pv,DOWN)),
            Write(n.next_to(r,DOWN)),
            Write(t.next_to(n,DOWN)),
        )
        self.wait(1)

        self.play(
            ReplacementTransform(FVEq,limOfFV)
        )
        self.wait(1)

        self.play(given.animate.to_edge(UP+LEFT))
        self.wait(1)

        self.play(Write(step1))
        self.wait(1)
        self.play(ReplacementTransform(step1,step2))
        self.wait(1)
        self.play(ReplacementTransform(step2,step3))
        self.wait(1)
        self.play(ReplacementTransform(step3,step4))
        self.wait(1)
        self.play(ReplacementTransform(step4,step5))
        self.wait(1)
        self.play(ReplacementTransform(step5,step6))
        self.wait(1)
        self.play(ReplacementTransform(step6,step7))
        self.wait(1)

        self.play(
            FadeOut(step7),
            FadeOut(given)
        )
        self.wait()

        self.play(Write(finalAns))
        self.wait(3)
        self.play(Unwrite(finalAns))
        self.wait()

class Q1Tabular(Scene):
    def construct(self):
        
        #VARS1

        approachT = Tex('Tabular Approach')
        x1 = 6.9
        x2 = 6.99
        x3 = 6.999
        c =  7
        x5 = 7.001
        x6 = 7.01
        x7 = 7.1

        b1 = 84.264
        b2 = 88.452
        b3 = 88.878
        b = 88.93
        b5 = 88.973
        b6 = 89.402
        b7 = 93.770
        finalAns = MathTex('\\lim_{x\\to7}{ \\frac{ {x}^{4} }{ {4}^{2}+{2}^{2}+{x} } } \\approx 89 \\ ')

        table = MathTable(
            [
                ["x",x1,x2,x3,c,x5,x6,x7],
                ["b","?","?","?","?","?","?","?"]
            ],
            include_outer_lines=True
        ).scale(0.6)

        finishedtable = MathTable(
            [
                ["x",x1,x2,x3,c,x5,x6,x7],
                ["b",b1,b2,b3,b,b5,b6,b7]
            ],
            include_outer_lines=True
        ).scale(0.6)

        #SCENES1

        self.play(Write(approachT))
        self.wait(2)
        self.play(Unwrite(approachT))
        self.wait(0.5)

        self.play(Create(table))
        self.wait(4)
        self.play(ReplacementTransform(table,finishedtable))
        self.wait(4)

        self.play(FadeOut(finishedtable))
        self.wait(1)

        self.play(Write(finalAns))
        self.wait(3)
        self.play(Unwrite(finalAns))
        self.wait()

class Q2Tabular(Scene):
    def construct(self):
        
        #VARS1

        approachT = Tex('Tabular Approach')
        x1 = 6.7
        x2 = 6.8
        x3 = 6.9
        c =  7
        x5 = 7.1
        x6 = 7.2
        x7 = 7.3

        fv1 = 55275.79 
        fv2 = 55358.61
        fv3 = 55441.56
        fv = 55524.63
        fv5 = 55607.82
        fv6 = 55691.14
        fv7 = 55774.58
        finalAns = MathTex('\\lim_{t\\to7}{PV(1+\\frac{r}{n})^{nt}}=55,524.63')

        table = MathTable(
            [
                ["t",x1,x2,x3,c,x5,x6,x7],
                ["FV(t)","?","?","?","?","?","?","?"]
            ],
            include_outer_lines=True
        ).scale(0.5)

        finishedtable = MathTable(
            [
                ["x",x1,x2,x3,c,x5,x6,x7],
                ["b",fv1,fv2,fv3,fv,fv5,fv6,fv7]
            ],
            include_outer_lines=True
        ).scale(0.6)

        #SCENES1

        self.play(Write(approachT))
        self.wait(2)
        self.play(Unwrite(approachT))
        self.wait(0.5)

        self.play(Create(table))
        self.wait(4)
        self.play(ReplacementTransform(table,finishedtable))
        self.wait(4)

        self.play(FadeOut(finishedtable))
        self.wait(1)

        self.play(Write(finalAns))
        self.wait(3)
        self.play(Unwrite(finalAns))
        self.wait()

class Outro(Scene):
    def construct(self):
        
        #VARS

        thankYou = Tex('Thank you for watching!').scale(1.5)
        groupName = Tex("Limit of the Brain").scale(1.25)
        chua = Tex("Chua, Arliyah Carmen")
        dayao = Tex("Dayao, Sophia Nicole")
        mariano = Tex("Mariano, Eunice Reign")
        tabamo = Tex("Tabamo, Euan Jed")
        members = VGroup(chua,dayao,mariano,tabamo).arrange(DOWN)
        musicUsed = Text("Music by Vincent Rubinetti",font="CMU Serif")
        program = Tex("Animated using Manim Community Edition")
        programmer = Tex("Programmed and Edited by Tabamo, Euan Jed")
        programming = VGroup(program,programmer).arrange(DOWN)

        voicedby = Tex("Voices by:")
        voices = Text("Mariano, Eunice Reign\nChua, Arliyah Carmen\nDayao, Sophia Nicole",font="CMU Serif",line_spacing=1).scale(0.7)
        voiceovers = VGroup(voicedby, voices).arrange(DOWN)

        computationby = Tex("Computation by:")
        computation = Tex("Dayao, Sophia Nicole")
        comps = VGroup(computationby,computation).arrange(DOWN)


        #SCENES
        self.play(Write(thankYou))
        self.wait(2)

        self.play(FadeOut(thankYou))
        self.wait(1)

        self.play(Write(groupName),run_time=1.5)
        self.wait(0.5)
        self.play(groupName.animate.to_edge(UP))
        self.wait(1)
        
        self.play(Write(members),run_time=4)
        self.wait(2)

        self.play(
            FadeOut(groupName),
            FadeOut(members),
            run_time = 2
        )
        self.wait(2)

        self.play(Write(programming))
        self.wait(2)
        self.play(FadeOut(programming))
        self.wait()

        self.play(Write(voiceovers))
        self.wait(2)
        self.play(FadeOut(voiceovers))
        self.wait()

        self.play(Write(comps))
        self.wait(2)
        self.play(FadeOut(comps))
        self.wait()

        self.play(Write(musicUsed))
        self.wait(2)

        self.play(FadeOut(musicUsed))
        self.wait(1)


class BTS(Scene):
    def construct(self):

        #VARS

        BTS = Tex("Behind the Scenes")
        BTS2 = Tex("(mostly code...)").scale(0.7)

        bts = VGroup(BTS, BTS2).arrange(DOWN)
        
        #SCENES

        self.play(Write(BTS))
        self.wait(2)
        self.play(Write(BTS2))
        self.wait(1)
        self.play(FadeOut(bts))